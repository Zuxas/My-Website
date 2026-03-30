/**
 * card-tooltips.js — Team Resolve
 * Mouseover Scryfall image tooltips for any element with class "c"
 * Usage: <span class="c">Goblin Bombardment</span>
 * Fetches from Scryfall named API, caches results, shows image on hover.
 */

(function () {
  const cache = {};
  let tooltip = null;
  let currentRequest = null;

  // Create the tooltip element once
  function createTooltip() {
    const el = document.createElement('div');
    el.id = 'scry-tooltip';
    el.style.cssText = `
      position: fixed;
      z-index: 99999;
      pointer-events: none;
      display: none;
      border: 1px solid rgba(0,0,0,0.2);
      border-radius: 4px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.35);
      background: #1a1a1a;
      padding: 0;
      overflow: hidden;
      transition: opacity 0.12s ease;
      opacity: 0;
    `;
    const img = document.createElement('img');
    img.id = 'scry-tooltip-img';
    img.style.cssText = `
      display: block;
      width: 220px;
      height: auto;
      border-radius: 4px;
    `;
    const spinner = document.createElement('div');
    spinner.id = 'scry-tooltip-spinner';
    spinner.style.cssText = `
      width: 220px;
      height: 60px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'DM Mono', monospace;
      font-size: 10px;
      letter-spacing: 0.1em;
      color: rgba(242,237,230,0.4);
      text-transform: uppercase;
    `;
    spinner.textContent = 'Loading...';
    el.appendChild(spinner);
    el.appendChild(img);
    document.body.appendChild(el);
    return el;
  }

  function showTooltip(x, y) {
    tooltip.style.display = 'block';
    positionTooltip(x, y);
    requestAnimationFrame(() => { tooltip.style.opacity = '1'; });
  }

  function hideTooltip() {
    tooltip.style.opacity = '0';
    setTimeout(() => { tooltip.style.display = 'none'; }, 120);
  }

  function positionTooltip(x, y) {
    const img = document.getElementById('scry-tooltip-img');
    const w = img.offsetWidth || 220;
    const margin = 16;
    const vpW = window.innerWidth;
    const vpH = window.innerHeight;

    let left = x + margin;
    let top = y - 40;

    // Flip left if would overflow right
    if (left + w + margin > vpW) {
      left = x - w - margin;
    }
    // Clamp top
    const h = tooltip.offsetHeight || 307;
    if (top + h > vpH - margin) {
      top = vpH - h - margin;
    }
    if (top < margin) top = margin;

    tooltip.style.left = left + 'px';
    tooltip.style.top = top + 'px';
  }

  async function fetchCard(name) {
    if (cache[name]) return cache[name];

    const url = `https://api.scryfall.com/cards/named?exact=${encodeURIComponent(name)}`;
    try {
      const res = await fetch(url);
      if (!res.ok) {
        // Try fuzzy if exact fails
        const fuzzyUrl = `https://api.scryfall.com/cards/named?fuzzy=${encodeURIComponent(name)}`;
        const fuzzyRes = await fetch(fuzzyUrl);
        if (!fuzzyRes.ok) { cache[name] = null; return null; }
        const data = await fuzzyRes.json();
        cache[name] = data;
        return data;
      }
      const data = await res.json();
      cache[name] = data;
      return data;
    } catch (e) {
      cache[name] = null;
      return null;
    }
  }

  function getImageUri(data) {
    if (!data) return null;
    // Handle double-faced cards
    if (data.image_uris) return data.image_uris.normal;
    if (data.card_faces && data.card_faces[0].image_uris) {
      return data.card_faces[0].image_uris.normal;
    }
    return null;
  }

  function attachTooltip(el) {
    const cardName = el.dataset.card || el.textContent.trim();
    let mouseX = 0, mouseY = 0;

    el.addEventListener('mouseenter', async (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;

      const spinner = document.getElementById('scry-tooltip-spinner');
      const img = document.getElementById('scry-tooltip-img');

      // Show spinner first
      spinner.style.display = 'flex';
      img.style.display = 'none';
      img.src = '';
      showTooltip(mouseX, mouseY);

      // Cancel any in-flight request
      currentRequest = cardName;

      const data = await fetchCard(cardName);

      // If mouse moved to another card before this resolved, bail
      if (currentRequest !== cardName) return;

      const uri = getImageUri(data);
      if (uri) {
        img.onload = () => {
          spinner.style.display = 'none';
          img.style.display = 'block';
          positionTooltip(mouseX, mouseY);
        };
        img.src = uri;
      } else {
        // Card not found — show name
        spinner.textContent = cardName + ' — not found';
        spinner.style.display = 'flex';
        img.style.display = 'none';
      }
    });

    el.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      positionTooltip(mouseX, mouseY);
    });

    el.addEventListener('mouseleave', () => {
      currentRequest = null;
      hideTooltip();
    });
  }

  function init() {
    tooltip = createTooltip();

    // Attach to all .c elements (card references)
    document.querySelectorAll('.c').forEach(attachTooltip);

    // Watch for dynamically revealed content (matchup panels etc.)
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((m) => {
        m.addedNodes.forEach((node) => {
          if (node.nodeType === 1) {
            if (node.classList && node.classList.contains('c')) {
              attachTooltip(node);
            }
            node.querySelectorAll && node.querySelectorAll('.c').forEach(attachTooltip);
          }
        });
      });
    });
    observer.observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Global style for card references
  const style = document.createElement('style');
  style.textContent = `
    .c {
      border-bottom: 1px dotted rgba(0,0,0,0.25);
      cursor: default;
      white-space: nowrap;
    }
    .c:hover {
      border-bottom-color: currentColor;
    }
  `;
  document.head.appendChild(style);
})();
