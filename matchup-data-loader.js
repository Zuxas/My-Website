/**
 * matchup-data-loader.js
 * Fetches data/modern-matchups.json and patches matchup tables
 * in playbooks with real win rates from the MTG Meta Analyzer DB.
 *
 * Each matchup-table element needs:
 *   data-deck="Boros Energy"   (the playbook's own deck name in the DB)
 *   data-vs="Izzet Prowess"    (the opponent archetype name in the DB)
 *
 * Tables without these attributes are left untouched.
 */
(function() {
    const CLASSES = {
        good: 'v-good',
        even: 'v-even',
        hard: 'v-hard',
    };

    function verdictClass(wr) {
        if (wr >= 55) return CLASSES.good;
        if (wr >= 48) return CLASSES.even;
        return CLASSES.hard;
    }

    function verdictText(wr) {
        if (wr >= 60) return 'Heavily Favored';
        if (wr >= 55) return 'Favored';
        if (wr >= 52) return 'Slight Edge';
        if (wr >= 48) return 'Even';
        if (wr >= 45) return 'Slight Dog';
        if (wr >= 40) return 'Unfavored';
        return 'Heavily Unfavored';
    }

    function patchTable(table, wr, matches) {
        // Patch the WR cell (3rd td, index 2)
        const row = table.querySelector('tbody tr');
        if (!row) return;
        const tds = row.querySelectorAll('td');
        if (tds[2]) {
            tds[2].textContent = wr.toFixed(1) + '%';
            tds[2].title = matches + ' matches · MTG Meta Analyzer DB';
        }
        // Patch the verdict span (4th td)
        const span = row.querySelector('.verdict');
        if (span) {
            span.className = 'verdict ' + verdictClass(wr);
            span.textContent = verdictText(wr);
            span.title = wr.toFixed(1) + '% from ' + matches + ' real matches';
        }
    }

    function addDataBadge(table, matches) {
        // Add a small "★ real data" badge after the table
        const badge = document.createElement('div');
        badge.style.cssText = 'font-family:"DM Mono",monospace;font-size:9px;' +
            'color:rgba(90,82,72,0.5);letter-spacing:0.12em;text-transform:uppercase;' +
            'margin:-1px 0 6px;padding:3px 0;';
        badge.textContent = '★ real data · ' + matches.toLocaleString() + ' matches · melee.gg + mtgtop8';
        table.parentNode.insertBefore(badge, table.nextSibling);
    }

    // Defer until DOM is ready
    document.addEventListener('DOMContentLoaded', function() {
        // Detect which deck this playbook is for
        const tables = document.querySelectorAll('.matchup-table[data-deck][data-vs]');
        if (!tables.length) return;

        fetch('data/modern-matchups.json')
            .then(function(r) { return r.json(); })
            .then(function(data) {
                tables.forEach(function(table) {
                    const deck = table.getAttribute('data-deck');
                    const vs   = table.getAttribute('data-vs');
                    const matchups = (data.decks || {})[deck] || [];
                    const entry = matchups.find(function(m) { return m.vs === vs; });
                    if (entry) {
                        patchTable(table, entry.wr, entry.matches);
                        addDataBadge(table, entry.matches);
                    }
                });
            })
            .catch(function() {
                // Silently fail — playbooks still show their hardcoded estimates
            });
    });
})();
