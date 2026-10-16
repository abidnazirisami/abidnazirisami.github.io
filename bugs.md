---
layout: page
title: Reported Bugs
permalink: /bugs/
last_updated: "2026-10-16T14:15:41+00:00"
---

<div class="bugs-dashboard">
  <div class="bugs-hero-banner">
    <h1 class="bugs-hero-title">Reported Bugs</h1>
    <p class="bugs-hero-subtitle">A list of <strong>323 bugs and issues</strong> reported across <strong>11 open-source applications</strong> spanning deep learning frameworks (PyTorch, TensorFlow, JAX), LLM serving engines (vLLM, SGLang), databases (ArangoDB, PostgreSQL), compilers (Clang/LLVM, GCC), and system utilities (cronie, OpenSSH). <strong>66.3%</strong> have been confirmed or fixed upstream.</p>
    <div class="bugs-hero-meta">
      <span class="bugs-meta-pill">Last updated: 2026-10-16 14:15:41 UTC</span>
      <span class="bugs-meta-pill">11 Applications</span>
      <a class="bugs-sheet-link" href="https://docs.google.com/spreadsheets/d/1r03ajIybbPeLBqHdxbD54Qghwoy8NjL2weeh89vX7wM/edit?usp=sharing" target="_blank" rel="noopener noreferrer">Spreadsheet: Google Sheets ↗</a>
    </div>
  </div>

<div class="bugs-kpi-grid">
  <div class="bugs-kpi-card kpi-total-card">
    <div class="kpi-header">
      <span class="kpi-label">Total Reported</span>
    </div>
    <div class="kpi-number">323</div>
    <div class="kpi-total-sub">
      <span class="kpi-total-item"><strong>11</strong> applications</span>
      <span class="kpi-total-divider"></span>
      <span class="kpi-total-item"><strong>66.3%</strong> confirmed or fixed</span>
    </div>
  </div>
  <div class="bugs-kpi-card kpi-confirmed-card">
    <div class="kpi-header">
      <span class="kpi-label">Confirmed</span>
    </div>
    <div class="kpi-number">177</div>
    <div class="kpi-sub">
      <span class="kpi-badge kpi-badge-confirmed">54.8%</span>
      <span>Triaged by maintainers</span>
    </div>
  </div>
  <div class="bugs-kpi-card kpi-fixed-card">
    <div class="kpi-header">
      <span class="kpi-label">Fixed Upstream</span>
    </div>
    <div class="kpi-number">37</div>
    <div class="kpi-sub">
      <span class="kpi-badge kpi-badge-fixed">11.5%</span>
      <span>Patched in releases</span>
    </div>
  </div>
  <div class="bugs-kpi-card kpi-pending-card">
    <div class="kpi-header">
      <span class="kpi-label">Under Review</span>
    </div>
    <div class="kpi-number">79</div>
    <div class="kpi-sub">
      <span class="kpi-badge kpi-badge-pending">24.5%</span>
      <span>Awaiting maintainer triage</span>
    </div>
  </div>
  <div class="bugs-kpi-card kpi-rejected-card">
    <div class="kpi-header">
      <span class="kpi-label">Rejected</span>
    </div>
    <div class="kpi-number">30</div>
    <div class="kpi-sub">
      <span class="kpi-badge kpi-badge-rejected">9.3%</span>
      <span>Closed as invalid or duplicate</span>
    </div>
  </div>
</div>


<div class="bugs-visuals-grid">
  <div class="bugs-chart-card">
    <div class="chart-card-header">
      <h3 class="chart-card-title">Reported Bugs by Application</h3>
      <div class="chart-legend">
        <span class="legend-item"><span class="legend-dot dot-confirmed"></span> Confirmed</span>
        <span class="legend-item"><span class="legend-dot dot-fixed"></span> Fixed</span>
        <span class="legend-item"><span class="legend-dot dot-pending"></span> Pending</span>
        <span class="legend-item"><span class="legend-dot dot-rejected"></span> Rejected</span>
      </div>
    </div>
    <div class="apps-bar-list">
      <div class="app-bar-row" title="PyTorch: 35 Confirmed, 27 Fixed, 10 Pending, 19 Rejected (91 total)" style="cursor: pointer;" onclick="toggleAppAccordion('pytorch')">
        <div class="app-bar-info">
          <span class="app-bar-name"><svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="PyTorch"><path d="M12.5 2.5C12.5 2.5 7.5 7.5 7.5 13.5C7.5 16.8 9.7 19.5 12.5 19.5C15.3 19.5 17.5 16.8 17.5 13.5C17.5 7.5 12.5 2.5 12.5 2.5Z" fill="#EE4C2C"/><circle cx="16.5" cy="7.5" r="1.8" fill="#EE4C2C"/></svg> <strong>PyTorch</strong> <span class="app-bar-domain">Deep Learning</span></span>
          <span class="app-bar-total">91 bugs</span>
        </div>
        <div class="app-bar-track">
          <div class="bar-segment seg-confirmed" style="width: 38.46%;"></div>
          <div class="bar-segment seg-fixed" style="width: 29.67%;"></div>
          <div class="bar-segment seg-pending" style="width: 10.99%;"></div>
          <div class="bar-segment seg-rejected" style="width: 20.88%;"></div>
        </div>
      </div>
      <div class="app-bar-row" title="TensorFlow: 39 Confirmed, 10 Fixed, 4 Pending, 8 Rejected (61 total)" style="cursor: pointer;" onclick="toggleAppAccordion('tensorflow')">
        <div class="app-bar-info">
          <span class="app-bar-name"><svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="TensorFlow"><path d="M12 2L3 7.2V17.5L7.5 15V9.8L12 7.2L16.5 9.8V15L21 17.5V7.2L12 2Z" fill="#FF6F00"/><path d="M10 10.5V22L14 22V10.5L12 9.3L10 10.5Z" fill="#FFA000"/></svg> <strong>TensorFlow</strong> <span class="app-bar-domain">Deep Learning</span></span>
          <span class="app-bar-total">61 bugs</span>
        </div>
        <div class="app-bar-track">
          <div class="bar-segment seg-confirmed" style="width: 42.86%;"></div>
          <div class="bar-segment seg-fixed" style="width: 10.99%;"></div>
          <div class="bar-segment seg-pending" style="width: 4.40%;"></div>
          <div class="bar-segment seg-rejected" style="width: 8.79%;"></div>
        </div>
      </div>
      <div class="app-bar-row" title="JAX: 28 Confirmed, 0 Fixed, 9 Pending, 1 Rejected (38 total)" style="cursor: pointer;" onclick="toggleAppAccordion('jax')">
        <div class="app-bar-info">
          <span class="app-bar-name"><svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="JAX"><rect x="2" y="4" width="20" height="16" rx="4" fill="#E8F0FE"/><text x="12" y="15.5" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="800" fill="#1A73E8" text-anchor="middle" letter-spacing="-0.02em">JAX</text></svg> <strong>JAX</strong> <span class="app-bar-domain">Autodiff / ML</span></span>
          <span class="app-bar-total">38 bugs</span>
        </div>
        <div class="app-bar-track">
          <div class="bar-segment seg-confirmed" style="width: 30.77%;"></div>
          <div class="bar-segment seg-fixed" style="width: 0.00%;"></div>
          <div class="bar-segment seg-pending" style="width: 9.89%;"></div>
          <div class="bar-segment seg-rejected" style="width: 1.10%;"></div>
        </div>
      </div>
      <div class="app-bar-row" title="vLLM: 27 Confirmed, 0 Fixed, 7 Pending, 0 Rejected (34 total)" style="cursor: pointer;" onclick="toggleAppAccordion('vllm')">
        <div class="app-bar-info">
          <span class="app-bar-name"><svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="vLLM"><path d="M4 4L12 20L20 4H15.5L12 13L8.5 4H4Z" fill="#2563EB"/><circle cx="12" cy="7" r="2.2" fill="#60A5FA"/></svg> <strong>vLLM</strong> <span class="app-bar-domain">LLM Serving</span></span>
          <span class="app-bar-total">34 bugs</span>
        </div>
        <div class="app-bar-track">
          <div class="bar-segment seg-confirmed" style="width: 29.67%;"></div>
          <div class="bar-segment seg-fixed" style="width: 0.00%;"></div>
          <div class="bar-segment seg-pending" style="width: 7.69%;"></div>
          <div class="bar-segment seg-rejected" style="width: 0.00%;"></div>
        </div>
      </div>
      <div class="app-bar-row" title="SGLang: 17 Confirmed, 0 Fixed, 15 Pending, 1 Rejected (33 total)" style="cursor: pointer;" onclick="toggleAppAccordion('sglang')">
        <div class="app-bar-info">
          <span class="app-bar-name"><svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="SGLang"><rect x="2" y="4" width="20" height="16" rx="4" fill="#F3E8FF"/><text x="12" y="15.5" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" font-weight="800" fill="#7C3AED" text-anchor="middle" letter-spacing="-0.02em">SGL</text></svg> <strong>SGLang</strong> <span class="app-bar-domain">LLM Serving</span></span>
          <span class="app-bar-total">33 bugs</span>
        </div>
        <div class="app-bar-track">
          <div class="bar-segment seg-confirmed" style="width: 18.68%;"></div>
          <div class="bar-segment seg-fixed" style="width: 0.00%;"></div>
          <div class="bar-segment seg-pending" style="width: 16.48%;"></div>
          <div class="bar-segment seg-rejected" style="width: 1.10%;"></div>
        </div>
      </div>
      <div class="app-bar-row" title="ArangoDB: 6 Confirmed, 0 Fixed, 18 Pending, 0 Rejected (24 total)" style="cursor: pointer;" onclick="toggleAppAccordion('arangodb')">
        <div class="app-bar-info">
          <span class="app-bar-name"><svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="ArangoDB"><path d="M12 2C8 2 4 8 4 14C4 18.5 7.5 22 12 22C16.5 22 20 18.5 20 14C20 8 16 2 12 2Z" fill="#2B8236"/><circle cx="12" cy="15" r="4.2" fill="#84CC16"/><circle cx="12" cy="15" r="2.5" fill="#65A30D"/></svg> <strong>ArangoDB</strong> <span class="app-bar-domain">Graph Database</span></span>
          <span class="app-bar-total">24 bugs</span>
        </div>
        <div class="app-bar-track">
          <div class="bar-segment seg-confirmed" style="width: 6.59%;"></div>
          <div class="bar-segment seg-fixed" style="width: 0.00%;"></div>
          <div class="bar-segment seg-pending" style="width: 19.78%;"></div>
          <div class="bar-segment seg-rejected" style="width: 0.00%;"></div>
        </div>
      </div>
      <div class="app-bar-row" title="cronie: 13 Confirmed, 0 Fixed, 0 Pending, 0 Rejected (13 total)" style="cursor: pointer;" onclick="toggleAppAccordion('cronie')">
        <div class="app-bar-info">
          <span class="app-bar-name"><svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="cronie"><circle cx="12" cy="12" r="9" stroke="#475569" stroke-width="2" fill="none"/><polyline points="12,7 12,12 15,14" stroke="#475569" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg> <strong>cronie</strong> <span class="app-bar-domain">System Daemon</span></span>
          <span class="app-bar-total">13 bugs</span>
        </div>
        <div class="app-bar-track">
          <div class="bar-segment seg-confirmed" style="width: 14.29%;"></div>
          <div class="bar-segment seg-fixed" style="width: 0.00%;"></div>
          <div class="bar-segment seg-pending" style="width: 0.00%;"></div>
          <div class="bar-segment seg-rejected" style="width: 0.00%;"></div>
        </div>
      </div>
      <div class="app-bar-row" title="PostgreSQL: 2 Confirmed, 0 Fixed, 8 Pending, 0 Rejected (10 total)" style="cursor: pointer;" onclick="toggleAppAccordion('postgresql')">
        <div class="app-bar-info">
          <span class="app-bar-name"><svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="PostgreSQL"><path d="M12 3C8 3 4 5 4 10C4 13.5 5.5 17 8 19V22H11V18H13V22H16V19C18.5 17 20 13.5 20 10C20 5 16 3 12 3Z" fill="#336791"/><circle cx="9.5" cy="9.5" r="1.5" fill="#FFFFFF"/><circle cx="14.5" cy="9.5" r="1.5" fill="#FFFFFF"/><path d="M11 12H13V15H11V12Z" fill="#E2E8F0"/></svg> <strong>PostgreSQL</strong> <span class="app-bar-domain">Database Engine</span></span>
          <span class="app-bar-total">10 bugs</span>
        </div>
        <div class="app-bar-track">
          <div class="bar-segment seg-confirmed" style="width: 2.20%;"></div>
          <div class="bar-segment seg-fixed" style="width: 0.00%;"></div>
          <div class="bar-segment seg-pending" style="width: 8.79%;"></div>
          <div class="bar-segment seg-rejected" style="width: 0.00%;"></div>
        </div>
      </div>
      <div class="app-bar-row" title="Clang / LLVM: 6 Confirmed, 0 Fixed, 3 Pending, 0 Rejected (9 total)" style="cursor: pointer;" onclick="toggleAppAccordion('clang_llvm')">
        <div class="app-bar-info">
          <span class="app-bar-name"><svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Clang / LLVM"><path d="M4 18C4 18 7 19 10 16C13 13 13 8 13 8C13 8 15 11 17 12C19 13 21 12 21 12C21 12 19 15 16 17C13 19 8 20 4 18Z" fill="#D9381E"/><path d="M13 8C11 5 7 4 7 4C7 4 8 7 10 9C11 10 13 8 13 8Z" fill="#EA580C"/></svg> <strong>Clang / LLVM</strong> <span class="app-bar-domain">Compiler / Toolchain</span></span>
          <span class="app-bar-total">9 bugs</span>
        </div>
        <div class="app-bar-track">
          <div class="bar-segment seg-confirmed" style="width: 6.59%;"></div>
          <div class="bar-segment seg-fixed" style="width: 0.00%;"></div>
          <div class="bar-segment seg-pending" style="width: 3.30%;"></div>
          <div class="bar-segment seg-rejected" style="width: 0.00%;"></div>
        </div>
      </div>
      <div class="app-bar-row" title="GCC: 3 Confirmed, 0 Fixed, 1 Pending, 1 Rejected (5 total)" style="cursor: pointer;" onclick="toggleAppAccordion('gcc')">
        <div class="app-bar-info">
          <span class="app-bar-name"><svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="GCC"><rect x="2" y="4" width="20" height="16" rx="4" fill="#FEE2E2"/><text x="12" y="15.5" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" font-weight="800" fill="#991B1B" text-anchor="middle" letter-spacing="-0.02em">GCC</text></svg> <strong>GCC</strong> <span class="app-bar-domain">Compiler / Toolchain</span></span>
          <span class="app-bar-total">5 bugs</span>
        </div>
        <div class="app-bar-track">
          <div class="bar-segment seg-confirmed" style="width: 3.30%;"></div>
          <div class="bar-segment seg-fixed" style="width: 0.00%;"></div>
          <div class="bar-segment seg-pending" style="width: 1.10%;"></div>
          <div class="bar-segment seg-rejected" style="width: 1.10%;"></div>
        </div>
      </div>
      <div class="app-bar-row" title="OpenSSH: 1 Confirmed, 0 Fixed, 4 Pending, 0 Rejected (5 total)" style="cursor: pointer;" onclick="toggleAppAccordion('openssh')">
        <div class="app-bar-info">
          <span class="app-bar-name"><svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="OpenSSH"><path d="M12 2L4 6V12C4 17 7.5 21 12 22C16.5 21 20 17 20 12V6L12 2Z" fill="#0F766E"/><circle cx="12" cy="10" r="2.5" fill="#CCFBF1"/><path d="M11 12.5H13V16H11V12.5Z" fill="#CCFBF1"/></svg> <strong>OpenSSH</strong> <span class="app-bar-domain">Security / Network</span></span>
          <span class="app-bar-total">5 bugs</span>
        </div>
        <div class="app-bar-track">
          <div class="bar-segment seg-confirmed" style="width: 1.10%;"></div>
          <div class="bar-segment seg-fixed" style="width: 0.00%;"></div>
          <div class="bar-segment seg-pending" style="width: 4.40%;"></div>
          <div class="bar-segment seg-rejected" style="width: 0.00%;"></div>
        </div>
      </div>
    </div>
  </div>
  <div class="bugs-chart-card">
    <div class="chart-card-header">
      <h3 class="chart-card-title">Resolution Status</h3>
      <span class="kpi-badge kpi-badge-confirmed">66.3% Confirmed + Fixed</span>
    </div>
    <div class="donut-chart-container">
      <canvas id="statusDonutChart" width="220" height="220" style="max-height: 220px;"></canvas>
      <div class="donut-center-stat">
        <div class="donut-center-number">214</div>
        <div class="donut-center-label">Confirmed &amp; Fixed</div>
      </div>
    </div>
    <div class="status-stat-pills">
      <div class="status-stat-item stat-item-confirmed"><span><span class="status-dot dot-confirmed"></span> Confirmed</span> <strong>177 (54.8%)</strong></div>
      <div class="status-stat-item stat-item-fixed"><span><span class="status-dot dot-fixed"></span> Fixed</span> <strong>37 (11.5%)</strong></div>
      <div class="status-stat-item stat-item-pending"><span><span class="status-dot dot-pending"></span> Pending</span> <strong>79 (24.5%)</strong></div>
      <div class="status-stat-item stat-item-rejected"><span><span class="status-dot dot-rejected"></span> Rejected</span> <strong>30 (9.3%)</strong></div>
    </div>
    <div class="bug-types-cloud">
      <div class="bug-types-title">Classification by Bug Type</div>
      <div class="bug-types-tags">
        <span class="bug-type-tag">Functional <span class="bug-type-count">158</span></span>
        <span class="bug-type-tag">Crash <span class="bug-type-count">88</span></span>
        <span class="bug-type-tag">Inconsistent <span class="bug-type-count">46</span></span>
        <span class="bug-type-tag">False positive <span class="bug-type-count">22</span></span>
        <span class="bug-type-tag">Overflow <span class="bug-type-count">3</span></span>
        <span class="bug-type-tag">Silent <span class="bug-type-count">2</span></span>
        <span class="bug-type-tag">Nan <span class="bug-type-count">2</span></span>
        <span class="bug-type-tag">Internal exception <span class="bug-type-count">2</span></span>
      </div>
    </div>
  </div>
</div>


<div class="bugs-toolbar">
  <div class="bugs-search-box">
    <span aria-hidden="true" style="color: #64748b; font-size: 0.9rem;">🔍</span>
    <input type="text" id="bugSearchInput" class="bugs-search-input" placeholder="Search by API, keyword, or title..." aria-label="Search bugs">
  </div>
  <div class="bugs-filter-group">
    <button class="filter-btn active" data-filter="all">All (323)</button>
    <button class="filter-btn" data-filter="Confirmed"><span class="filter-dot dot-confirmed"></span>Confirmed (177)</button>
    <button class="filter-btn" data-filter="Fixed"><span class="filter-dot dot-fixed"></span>Fixed (37)</button>
    <button class="filter-btn" data-filter="Pending"><span class="filter-dot dot-pending"></span>Pending (79)</button>
    <button class="filter-btn" data-filter="Rejected"><span class="filter-dot dot-rejected"></span>Rejected (30)</button>
  </div>
  <div class="bugs-action-group">
    <button class="action-btn" id="expandAllBtn">Expand All</button>
    <button class="action-btn" id="collapseAllBtn">Collapse All</button>
    <span style="font-size: 0.8rem; color: #64748b; font-weight: 500; margin-left: 4px;">Showing <strong id="visibleCount" style="color: #0f172a;">323</strong> of 323</span>
  </div>
</div>
<div id="noBugsMessage" class="no-bugs-found">No reported bugs matched your filter or search query.</div>


<div class="bugs-apps-accordion">
<details class="app-collapsible-card" id="app-pytorch" data-app="pytorch">
  <summary class="app-summary">
    <div class="app-summary-left">
      <svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="PyTorch"><path d="M12.5 2.5C12.5 2.5 7.5 7.5 7.5 13.5C7.5 16.8 9.7 19.5 12.5 19.5C15.3 19.5 17.5 16.8 17.5 13.5C17.5 7.5 12.5 2.5 12.5 2.5Z" fill="#EE4C2C"/><circle cx="16.5" cy="7.5" r="1.8" fill="#EE4C2C"/></svg>
      <span class="app-name-text">PyTorch</span>
      <span class="app-domain-pill">Deep Learning</span>
      <span class="app-count-badge">91 bugs</span>
    </div>
    <div class="app-summary-right">
      <div class="app-pills-row">
        <span class="mini-status-pill mini-confirmed">35 Confirmed</span>
        <span class="mini-status-pill mini-fixed">27 Fixed</span>
        <span class="mini-status-pill mini-pending">10 Pending</span>
        <span class="mini-status-pill mini-rejected">19 Rejected</span>
      </div>
      <span class="app-chevron-icon" aria-hidden="true">▼</span>
    </div>
  </summary>
  <div class="app-details-body">
    <div class="bugs-cards-list">
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.logcumsumexp torch.logcumsumexp runtime error inconsistency on cpu and cuda (also documentation missing constraint) inconsistent centaur https://github.com/pytorch/pytorch/issues/139342  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.logcumsumexp</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">torch.logcumsumexp runtime error inconsistency on CPU and CUDA (also documentation missing constraint)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/139342" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #139342 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.nn.functional.conv_transpose2d torch.nn.functional.conv_transpose2d produces inconsistent output on cpu and cuda inconsistent centaur https://github.com/pytorch/pytorch/issues/153276  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.nn.functional.conv_transpose2d</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-flag-pill">Not a bug</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">torch.nn.functional.conv_transpose2d produces inconsistent output on CPU and CUDA</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153276" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153276 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.nn.functional.conv_transpose2d `torch.nn.functional.conv_transpose2d` has inconsistent handling of `float16` overflow on cpu overflow centaur https://github.com/pytorch/pytorch/issues/153700  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.nn.functional.conv_transpose2d</span>
            <span class="bug-type-pill">Overflow</span>
            <span class="bug-flag-pill">Duplicate</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`torch.nn.functional.conv_transpose2d` has inconsistent handling of `float16` overflow on CPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153700" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153700 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.add inconsistent float16 overflow behavior between cpu and cuda devices inconsistent flashfuzz https://github.com/pytorch/pytorch/issues/152731  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.add</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Inconsistent float16 overflow behavior between CPU and CUDA devices</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/152731" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #152731 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.lcm_ fpe when using `torch.lcm_` with int32 tensor and int16 scalar crash flashfuzz https://github.com/pytorch/pytorch/issues/152979  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.lcm_</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">FPE when using `torch.lcm_` with int32 tensor and int16 scalar</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/152979" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #152979 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.clamp_min inconsistent overflow handling in `torch.clamp_min` between cpu and cuda for float16 tensors inconsistent flashfuzz https://github.com/pytorch/pytorch/issues/153187  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.clamp_min</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Inconsistent overflow handling in `torch.clamp_min` between CPU and CUDA for float16 tensors</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153187" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153187 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.fmod fpe crash in torch.fmod with large negative integer modulo value crash flashfuzz https://github.com/pytorch/pytorch/issues/153203  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.fmod</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">FPE Crash in torch.fmod with large negative integer modulo value</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153203" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153203 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.cosine_similarity inconsistent error handling between cpu and cuda for `cosine_similarity` inconsistent flashfuzz https://github.com/pytorch/pytorch/issues/153209 https://github.com/pytorch/pytorch/pull/169047 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.cosine_similarity</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Inconsistent Error Handling Between CPU and CUDA for `cosine_similarity`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153209" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153209 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/169047" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #169047 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.addcmul inconsistent error handling in `torch.addcmul` with `int16` tensors inconsistent flashfuzz https://github.com/pytorch/pytorch/issues/153210  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.addcmul</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Inconsistent Error Handling in `torch.addcmul` with `int16` Tensors</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153210" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153210 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.native_channel_shuffle `torch.native_channel_shuffle` crashes with floating point exception when given large integer parameter crash flashfuzz https://github.com/pytorch/pytorch/issues/153231  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.native_channel_shuffle</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">`torch.native_channel_shuffle` crashes with Floating Point Exception when given large integer parameter</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153231" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153231 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.pixel_shuffle() fpe when calling `torch.pixel_shuffle()` with empty tensors and large upscale_factor crash flashfuzz https://github.com/pytorch/pytorch/issues/153327  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.pixel_shuffle()</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">FPE when calling `torch.pixel_shuffle()` with empty tensors and large upscale_factor</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153327" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153327 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.to_dense() segmentation fault when converting sparse coo tensor with complex values to dense crash flashfuzz https://github.com/pytorch/pytorch/issues/153329  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.to_dense()</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Segmentation fault when converting sparse COO tensor with complex values to dense</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153329" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153329 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.combinations `torch.combinations` exhibits excessive memory usage and hangs for moderate `n` and `r` due to `n^r` crash flashfuzz https://github.com/pytorch/pytorch/issues/153337  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.combinations</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">`torch.combinations` exhibits excessive memory usage and hangs for moderate `n` and `r` due to `n^r`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153337" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153337 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.dequantize torch.dequantize result inconsistent on cpu and gpu inconsistent flashfuzz https://github.com/pytorch/pytorch/issues/153358  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.dequantize</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">torch.dequantize result inconsistent on CPU and GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153358" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153358 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.aminmax torch.aminmax reducing over all dims should not accept keepdim inconsistent flashfuzz https://github.com/pytorch/pytorch/issues/153360  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.aminmax</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">torch.aminmax reducing over all dims should not accept keepdim</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153360" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153360 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.batch_norm_update_stats memory corruption in `torch.batch_norm_update_stats` crash flashfuzz https://github.com/pytorch/pytorch/issues/153967  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.batch_norm_update_stats</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Memory Corruption in `torch.batch_norm_update_stats`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153967" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153967 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.nn.instancenorm3d torch.nn.instancenorm3d producing inconsistent output for float16 tensors on cpu and gpu inconsistent greyfox https://github.com/pytorch/pytorch/issues/136680 https://github.com/pytorch/pytorch/pull/136824 confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.nn.InstanceNorm3d</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.nn.InstanceNorm3d producing inconsistent output for float16 tensors on CPU and GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/136680" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #136680 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/136824" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #136824 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.dot torch.dot has inconsistent support for int64 (long) crash greyfox https://github.com/pytorch/pytorch/issues/138829  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.dot</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.dot has inconsistent support for int64 (long)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/138829" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #138829 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.nn.instancenorm2d torch.nn.instancenorm2d throws &quot;mixed dtype&quot; error with track_running_stats set to true crash greyfox https://github.com/pytorch/pytorch/issues/139140  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.nn.InstanceNorm2d</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-flag-pill">Not a bug</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.nn.InstanceNorm2d throws &quot;mixed dtype&quot; error with track_running_stats set to True</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/139140" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #139140 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.nn.reflectionpad2d torch.nn.reflectionpad2d throws cuda error on large tensors crash greyfox https://github.com/pytorch/pytorch/issues/139333  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.nn.ReflectionPad2d</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.nn.ReflectionPad2d throws CUDA error on large tensors</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/139333" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #139333 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.logcumsumexp torch.logcumsumexp runtime error inconsistency on cpu and cuda (also documentation missing constraint) crash greyfox https://github.com/pytorch/pytorch/issues/139342  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.logcumsumexp</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.logcumsumexp runtime error inconsistency on CPU and CUDA (also documentation missing constraint)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/139342" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #139342 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.tensor.resize_ `resize_` updates tensor shape metadata even when storage resize fails, creating corrupted &quot;zombie&quot; tensors crash rbf https://github.com/pytorch/pytorch/issues/170298  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.Tensor.resize_</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`resize_` updates tensor shape metadata even when storage resize fails, creating corrupted &quot;Zombie&quot; tensors</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/170298" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #170298 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.nn.functional.pixel_shuffle `torch.nn.functional.pixel_shuffle` throws sigfpe (floating point exception) with large upscale_factor crash rbf https://github.com/pytorch/pytorch/issues/171838 https://github.com/pytorch/pytorch/pull/171855 confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.nn.functional.pixel_shuffle</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.nn.functional.pixel_shuffle` throws SIGFPE (Floating Point Exception) with large upscale_factor</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/171838" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #171838 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/171855" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #171855 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.nn.nllloss `torch.nn.nllloss` has inconsistent error handling: cuda skips type check for empty inputs vs cpu inconsistent rbf https://github.com/pytorch/pytorch/issues/171931 https://github.com/pytorch/pytorch/pull/172018 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.nn.NLLLoss</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.nn.NLLLoss` has inconsistent error handling: CUDA skips type check for empty inputs vs CPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/171931" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #171931 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/172018" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #172018 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.pixel_shuffle torch.pixel_shuffle cpu-gpu crash with massive upscale factor overflow rbf https://github.com/pytorch/pytorch/issues/172011  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.pixel_shuffle</span>
            <span class="bug-type-pill">Overflow</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">torch.pixel_shuffle CPU-GPU crash with massive upscale factor</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/172011" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #172011 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.fbgemm_linear_quantize_weight, torch.fbgemm_pack_gemm_matrix_fp16 `torch.fbgemm_linear_quantize_weight` crashes with segmentation fault (sigsegv) with a cuda tensor crash rbf https://github.com/pytorch/pytorch/issues/173495 https://github.com/pytorch/pytorch/pull/173682 confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.fbgemm_linear_quantize_weight, torch.fbgemm_pack_gemm_matrix_fp16</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.fbgemm_linear_quantize_weight` crashes with segmentation fault (SIGSEGV) with a cuda tensor</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/173495" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #173495 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/173682" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #173682 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch._stack `torch._stack` crashes with segmentation fault (`sigsegv`) on empty tensors crash rbf https://github.com/pytorch/pytorch/issues/173498  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch._stack</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-flag-pill">Not a bug</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch._stack` crashes with segmentation fault (`SIGSEGV`) on empty tensors</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/173498" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #173498 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.native_channel_shuffle `torch.native_channel_shuffle` crashes with fpe on gpu when `groups=0` crash rbf https://github.com/pytorch/pytorch/issues/173500 https://github.com/pytorch/pytorch/pull/181029 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.native_channel_shuffle</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.native_channel_shuffle` crashes with FPE on GPU when `groups=0`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/173500" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #173500 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/181029" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #181029 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.arange `torch.arange` triggers `sigfpe` (floating point exception) instead of runtimeerror when writing float results to `int64` out tensor crash rbf https://github.com/pytorch/pytorch/issues/173574 https://github.com/pytorch/pytorch/pull/173601 confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.arange</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.arange` triggers `SIGFPE` (Floating Point Exception) instead of RuntimeError when writing float results to `int64` out tensor</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/173574" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #173574 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/173601" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #173601 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.special.zeta, torch.special.spherical_bessel_j0,  torch.special.i1, torch.special.modified_bessel_k0, torch.special.sinc, torch.special.psi, torch.special.modified_bessel_i1, torch.special.entr, torch.special.i1e, torch.special.log_ndtr, torch.special.i0, torch.special.hermite_polynomial_he, torch.special.i0e, torch.special.gammaln, torch.lgamma `torch.special.zeta` returns incorrect output with `uint16` on cuda, along with many other `torch.special` apis inconsistent rbf https://github.com/pytorch/pytorch/issues/173636 https://github.com/pytorch/pytorch/pull/174303 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.special.zeta, torch.special.spherical_bessel_j0,  torch.special.i1, torch.special.modified_bessel_k0, torch.special.sinc, torch.special.psi, torch.special.modified_bessel_i1, torch.special.entr, torch.special.i1e, torch.special.log_ndtr, torch.special.i0, torch.special.hermite_polynomial_he, torch.special.i0e, torch.special.gammaln, torch.lgamma</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.special.zeta` returns incorrect output with `uint16` on CUDA, along with many other `torch.special` APIs</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/173636" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #173636 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/174303" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #174303 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.linalg.slogdet, torch.linalg.inv, torch.inverse `torch.linalg.slogdet` does not propagate `nan` in cuda inconsistent rbf https://github.com/pytorch/pytorch/issues/173638  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.linalg.slogdet, torch.linalg.inv, torch.inverse</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.linalg.slogdet` does not propagate `NaN` in CUDA</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/173638" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #173638 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.logdet torch.logdet produces incorrect results for singular matrices on cuda vs cpu inconsistent rbf https://github.com/pytorch/pytorch/issues/154312  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.logdet</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">torch.logdet produces incorrect results for singular matrices on CUDA vs CPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/154312" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #154312 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch._remove_batch_dim segmentation fault (core dumped) in `torch._remove_batch_dim` crash rbf https://github.com/pytorch/pytorch/issues/128691 https://github.com/pytorch/pytorch/pull/139016 confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch._remove_batch_dim</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">Segmentation fault (core dumped) in `torch._remove_batch_dim`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/128691" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #128691 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/139016" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #139016 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.lcm floating point exception on torch.lcm crash rbf https://github.com/pytorch/pytorch/issues/121343  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.lcm</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">Floating point exception on torch.lcm</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/121343" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #121343 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.floor_divide `torch.floor_divide` crashes with floating point exception (`sigfpe`) when dividing `int64_min` crash rbf https://github.com/pytorch/pytorch/issues/173506  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.floor_divide</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.floor_divide` crashes with Floating point exception (`SIGFPE`) when dividing `INT64_MIN`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/173506" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #173506 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch._c._nn.slow_conv3d segmentation fault due to empty stride argument in `torch._c._nn.slow_conv3d` crash rbf https://github.com/pytorch/pytorch/issues/121095 https://github.com/pytorch/pytorch/pull/181063 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch._C._nn.slow_conv3d</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">Segmentation Fault Due to Empty Stride Argument in `torch._C._nn.slow_conv3d`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/121095" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #121095 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/181063" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #181063 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch.addcmul feedback about torch.addcdiv silent rbf https://github.com/pytorch/pytorch/issues/170869  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch.addcmul</span>
            <span class="bug-type-pill">Silent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">Feedback about torch.addcdiv</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/170869" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #170869 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.nn.functional.softshrink torch.nn.functional.softshrink throws overflow error on cuda but not on cpu overflow centaur https://github.com/pytorch/pytorch/issues/153186  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.nn.functional.softshrink</span>
            <span class="bug-type-pill">Overflow</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">torch.nn.functional.softshrink throws overflow error on CUDA but not on CPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153186" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153186 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.nn.functional.rrelu `torch.nn.functional.rrelu` crashes on cpu with `training=true` when `lower` or `upper` is set to `inf` inconsistent centaur https://github.com/pytorch/pytorch/issues/153281  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.nn.functional.rrelu</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`torch.nn.functional.rrelu` crashes on CPU with `training=True` when `lower` or `upper` is set to `inf`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153281" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153281 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.native_channel_shuffle `torch.native_channel_shuffle` throws fpe when `groups` &gt; size of the second dimension of the input tensor crash centaur https://github.com/pytorch/pytorch/issues/158154  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.native_channel_shuffle</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`torch.native_channel_shuffle` throws FPE when `groups` &gt; size of the second dimension of the input tensor</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/158154" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #158154 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.nn.lppool2d `torch.nn.lppool2d` throws inconsistent error on cpu and gpu inconsistent centaur https://github.com/pytorch/pytorch/issues/158166  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.nn.LPPool2d</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`torch.nn.LPPool2d` throws inconsistent error on CPU and GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/158166" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #158166 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.nn.functional.normalize torch.nn.functional.normalize producing nan values with a large p value and tensor of complex numbers nan centaur https://github.com/pytorch/pytorch/issues/135428 https://github.com/pytorch/pytorch/pull/140375 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.nn.functional.normalize</span>
            <span class="bug-type-pill">Nan</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">torch.nn.functional.normalize producing nan values with a large p value and tensor of complex numbers</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/135428" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #135428 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/140375" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #140375 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.nanmean inconsistent behavior and misleading error message for `torch.nanmean()`  with complex dtypes inconsistent flashfuzz https://github.com/pytorch/pytorch/issues/153132  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.nanmean</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Inconsistent behavior and misleading error message for `torch.nanmean()`  with complex dtypes</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153132" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153132 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.arange inconsistent behavior between cpu and gpu implementations of `torch.arange` inconsistent flashfuzz https://github.com/pytorch/pytorch/issues/153133  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.arange</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Inconsistent behavior between CPU and GPU implementations of `torch.arange`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153133" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153133 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.batch_norm `torch.batch_norm` shows inconsistent error behavior between cpu and gpu inconsistent flashfuzz https://github.com/pytorch/pytorch/issues/153137  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.batch_norm</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">`torch.batch_norm` shows inconsistent error behavior between CPU and GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153137" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153137 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.fused_moving_avg_obs_fake_quant iinconsistent error handling in `torch.fused_moving_avg_obs_fake_quant` between cpu and gpu implementations inconsistent flashfuzz https://github.com/pytorch/pytorch/issues/153310  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.fused_moving_avg_obs_fake_quant</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">IInconsistent Error Handling in `torch.fused_moving_avg_obs_fake_quant` Between CPU and GPU Implementations</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153310" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153310 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="lp_pool1d `lp_pool1d` behavior inconsistency between cpu and gpu inconsistent flashfuzz https://github.com/pytorch/pytorch/issues/153312  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">lp_pool1d</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">`lp_pool1d` behavior inconsistency between CPU and GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153312" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153312 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.choose_qparams_optimized segmentation fault when calling `torch.choose_qparams_optimized()` with empty tensors and extreme num_bins value crash flashfuzz https://github.com/pytorch/pytorch/issues/153326  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.choose_qparams_optimized</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Segmentation fault when calling `torch.choose_qparams_optimized()` with empty tensors and extreme num_bins value</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153326" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153326 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.remainder fpe  in `torch.remainder` crash flashfuzz https://github.com/pytorch/pytorch/issues/153919  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.remainder</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">FPE  in `torch.remainder`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153919" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153919 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.acos torch.acos produces different values using cpu and cuda for input with torch.complex128 dtype inconsistent greyfox https://github.com/pytorch/pytorch/issues/134487 https://github.com/pytorch/pytorch/pull/134838 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.acos</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.acos produces different values using cpu and cuda for input with torch.complex128 dtype</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/134487" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #134487 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/134838" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #134838 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.nn.replicationpad1d, torch.nn.reflectionpad1d,torch.nn.replicationpad3d, torch.nn.reflectionpad3d,torch.nn.replicationpad3d, torch.nn.reflectionpad3d torch.nn.replicationpad and torch.nn.reflectionpad does not support float16 crash greyfox https://github.com/pytorch/pytorch/issues/135519  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.nn.ReplicationPad1d, torch.nn.ReflectionPad1d,torch.nn.ReplicationPad3d, torch.nn.ReflectionPad3d,torch.nn.ReplicationPad3d, torch.nn.ReflectionPad3d</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.nn.ReplicationPad and torch.nn.ReflectionPad does not support float16</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/135519" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #135519 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.sigmoid torch.sigmoid producing nan for tensor of negative complex numbers on cpu nan greyfox https://github.com/pytorch/pytorch/issues/135777 https://github.com/pytorch/pytorch/pull/140391 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.sigmoid</span>
            <span class="bug-type-pill">Nan</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.sigmoid producing nan for tensor of negative complex numbers on cpu</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/135777" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #135777 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/140391" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #140391 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.asin torch.asin returns incorrect value with complex input on cpu inconsistent greyfox https://github.com/pytorch/pytorch/issues/138327 https://github.com/pytorch/pytorch/pull/134838 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.asin</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.asin returns incorrect value with complex input on cpu</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/138327" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #138327 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/134838" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #134838 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.histc torch.histc not checking min &gt; max on cuda for int8 tensors crash greyfox https://github.com/pytorch/pytorch/issues/139360 https://github.com/pytorch/pytorch/pull/139372 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.histc</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.histc not checking min &gt; max on cuda for int8 tensors</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/139360" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #139360 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/139372" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #139372 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.nn.logsoftmax `torch.nn.logsoftmax` produces inf value on cpu but not on gpu inconsistent centaur https://github.com/pytorch/pytorch/issues/158310  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.nn.LogSoftmax</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`torch.nn.LogSoftmax` produces inf value on CPU but not on GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/158310" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #158310 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.nn.functional.celu `torch.nn.functional.celu` produces inconsistent output on cpu vs cuda inconsistent centaur https://github.com/pytorch/pytorch/issues/158314  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.nn.functional.celu</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`torch.nn.functional.celu` produces inconsistent output on CPU vs CUDA</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/158314" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #158314 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.floor_divide `torch.floor_divide` causes inconsistent precision false positive centaur https://github.com/pytorch/pytorch/issues/153597  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.floor_divide</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`torch.floor_divide` causes inconsistent precision</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153597" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153597 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.fmin `torch.fmin` has inconsistent overflow behavior on cpu and gpu false positive centaur https://github.com/pytorch/pytorch/issues/158172  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.fmin</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`torch.fmin` has inconsistent overflow behavior on CPU and GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/158172" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #158172 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.det `torch.det` returns inconsistent results for complex tensor on cpu vs gpu false positive centaur https://github.com/pytorch/pytorch/issues/158208  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.det</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`torch.det` returns inconsistent results for complex tensor on CPU vs GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/158208" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #158208 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.tensor.put_ inconsistent behavior between cpu and gpu implementations of `torch.tensor.put_` method false positive flashfuzz https://github.com/pytorch/pytorch/issues/152755  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.Tensor.put_</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Inconsistent behavior between CPU and GPU implementations of `torch.Tensor.put_` method</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/152755" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #152755 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.tensor.asin_ inconsistent complex torch.tensor.asin() results between cpu and gpu false positive flashfuzz https://github.com/pytorch/pytorch/issues/153128  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.Tensor.asin_</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Inconsistent Complex torch.Tensor.asin() Results Between CPU and GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153128" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153128 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.lu_unpack segmentation fault in torch.lu_unpack() with bfloat16 tensor false positive flashfuzz https://github.com/pytorch/pytorch/issues/153232  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.lu_unpack</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Segmentation Fault in torch.lu_unpack() with bfloat16 Tensor</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153232" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153232 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.cumsum `torch.cumsum()` on bfloat16 tensor with dtype=torch.int8 produce inconsistent results between cpu and gpu false positive flashfuzz https://github.com/pytorch/pytorch/issues/153359  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.cumsum</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">`torch.cumsum()` on bfloat16 tensor with dtype=torch.int8 produce inconsistent results between CPU and GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/153359" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #153359 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.linalg.lstsq torch.linalg.lstsq generating different solutions on cpu and gpu false positive greyfox https://github.com/pytorch/pytorch/issues/136443  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.linalg.lstsq</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.linalg.lstsq generating different solutions on CPU and GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/136443" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #136443 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.digamma torch.digamma produces inconsistent result between cpu and gpu for 0.00615 (float16) false positive greyfox https://github.com/pytorch/pytorch/issues/137817  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.digamma</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.digamma produces inconsistent result between cpu and gpu for 0.00615 (float16)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/137817" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #137817 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.nansum torch.nansum does not work with complex numbers on cpu false positive greyfox https://github.com/pytorch/pytorch/issues/139349  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.nansum</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.nansum does not work with complex numbers on CPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/139349" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #139349 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.nn.localresponsenorm `torch.nn.localresponsenorm` raises `runtimeerror` on cpu for float16 inputs (parity issue with cuda) false positive rbf https://github.com/pytorch/pytorch/issues/171948  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.nn.LocalResponseNorm</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.nn.LocalResponseNorm` raises `RuntimeError` on CPU for float16 inputs (parity issue with CUDA)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/171948" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #171948 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.nn.linear torch.nn.linear shape mismatch with large/incompatible inpu false positive rbf https://github.com/pytorch/pytorch/issues/172014  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.nn.Linear</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">torch.nn.Linear shape mismatch with large/incompatible inpu</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/172014" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #172014 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.index_select torch.index_select out-of-bounds triggers inconsistent runtime errors false positive rbf https://github.com/pytorch/pytorch/issues/172019  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.index_select</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">torch.index_select out-of-bounds triggers inconsistent runtime errors</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/172019" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #172019 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.addr `torch.addr`: cpu/gpu inconsistency with `int64` input and `float16` vector (cpu returns `inf`, gpu returns valid values) false positive rbf https://github.com/pytorch/pytorch/issues/173491  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.addr</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.addr`: CPU/GPU Inconsistency with `int64` input and `float16` vector (CPU returns `inf`, GPU returns valid values)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/173491" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #173491 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.angle torch.angle cuda version not implemented for bfloat16 and half (float16) crash greyfox https://github.com/pytorch/pytorch/issues/134607 https://github.com/pytorch/pytorch/pull/191301 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.angle</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.angle cuda version not implemented for bfloat16 and half (float16)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/134607" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #134607 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/191301" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #191301 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="torch.floor_divide torch.floor_divide not triggering zerodivisionerror on gpu inconsistent greyfox https://github.com/pytorch/pytorch/issues/135330  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">torch.floor_divide</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.floor_divide not triggering ZeroDivisionError on GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/135330" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #135330 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="torch.nn.avgpool2d torch.nn.avgpool2d works with long on cpu but not gpu crash greyfox https://github.com/pytorch/pytorch/issues/139115  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">torch.nn.AvgPool2d</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">torch.nn.AvgPool2d works with long on cpu but not gpu</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/139115" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #139115 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="torch.add, torch.matmul, torch.linalg.pinv silent heap buffer overflow in standard ops (add, pinv) via implicit view resizing silent rbf https://github.com/pytorch/pytorch/issues/170573  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">torch.add, torch.matmul, torch.linalg.pinv</span>
            <span class="bug-type-pill">Silent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">Silent Heap Buffer Overflow in standard ops (add, pinv) via implicit view resizing</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/170573" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #170573 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="torch.clip `torch.clip` has checks for float16 scalar overflow on cpu but not on gpu inconsistent rbf https://github.com/pytorch/pytorch/issues/171356  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">torch.clip</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.clip` has checks for float16 scalar overflow on CPU but not on GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/171356" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #171356 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="torch.nn.pixelunshuffle `torch.nn.pixelunshuffle` throws runtimeerror: stride calculation overflowed on cuda with empty input and large downscale factor (cpu succeeds) inconsistent rbf https://github.com/pytorch/pytorch/issues/171536  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">torch.nn.PixelUnshuffle</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.nn.PixelUnshuffle` throws RuntimeError: Stride calculation overflowed on CUDA with empty input and large downscale factor (CPU succeeds)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/171536" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #171536 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="torch.linalg.cholesky_ex `torch.linalg.cholesky_ex`: inconsistency between cpu (inf) and cuda (nan) for infinite input, with silent nans on cuda inconsistent rbf https://github.com/pytorch/pytorch/issues/173786  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">torch.linalg.cholesky_ex</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-flag-pill">Not a bug</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.linalg.cholesky_ex`: Inconsistency between CPU (Inf) and CUDA (NaN) for infinite input, with silent NaNs on CUDA</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/173786" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #173786 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="torch.nn.functional.poissonnllloss `torch.nn.functional.poissonnllloss` returns `nan` imaginary part on cpu (vs 0 on gpu) for overflowing complex inputs inconsistent rbf https://github.com/pytorch/pytorch/issues/173796  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">torch.nn.functional.PoissonNLLLoss</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.nn.functional.PoissonNLLLoss` returns `NaN` imaginary part on CPU (vs 0 on GPU) for overflowing complex inputs</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/173796" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #173796 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="torch.nn.functional.pdist `torch.nn.functional.pdist` (p=0) with `inf` inputs produce wildly different values inconsistent rbf https://github.com/pytorch/pytorch/issues/173799 https://github.com/pytorch/pytorch/pull/173826 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">torch.nn.functional.pdist</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`torch.nn.functional.pdist` (p=0) with `inf` inputs produce wildly different values</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/173799" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #173799 ↗</a>
          <a href="https://github.com/pytorch/pytorch/pull/173826" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #173826 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch-ldexp;torch-ldexp--long torch.ldexp raises notimplementederror for a bool exponent (eager), while torch.compile and the decomposition accept it crash claude-opus-5 https://github.com/pytorch/pytorch/issues/198577  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch-ldexp;torch-ldexp--long</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">torch.ldexp raises NotImplementedError for a bool exponent (eager), while torch.compile and the decomposition accept it</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/198577" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #198577 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="torch-distributions-cauchy;torch-distributions-cauchy--long torch.distributions.cauchy.log_prob returns -inf (and nan gradients) for large |value - loc| / scale because the square overflows functional claude-opus-5 https://github.com/pytorch/pytorch/issues/198578  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">torch-distributions-cauchy;torch-distributions-cauchy--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">torch.distributions.Cauchy.log_prob returns -inf (and NaN gradients) for large |value - loc| / scale because the square overflows</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/198578" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #198578 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="torch-distributions-normal torch.distributions.normal.log_prob returns nan for very large or very small scale because scale**2 overflows/underflows functional claude-opus-5 https://github.com/pytorch/pytorch/issues/198579  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">torch-distributions-normal</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">torch.distributions.Normal.log_prob returns NaN for very large or very small scale because scale**2 overflows/underflows</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/198579" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #198579 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch-distributions-laplace torch.distributions.laplace cdf/icdf return a zero gradient at the median (value == loc, p == 0.5) functional claude-opus-5 https://github.com/pytorch/pytorch/issues/198580  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch-distributions-laplace</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">torch.distributions.Laplace cdf/icdf return a zero gradient at the median (value == loc, p == 0.5)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/198580" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #198580 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch-distributions-laplace torch.distributions.laplace.icdf returns -inf (and loses accuracy) for small tail probabilities functional claude-opus-5 https://github.com/pytorch/pytorch/issues/198582  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch-distributions-laplace</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">torch.distributions.Laplace.icdf returns -inf (and loses accuracy) for small tail probabilities</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/198582" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #198582 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch-special-bessel-y0;torch-special-bessel-j1;torch-special-bessel-y1;torch-special-bessel-j0;torch-special-airy-ai torch.special.bessel_j0 / bessel_j1 / bessel_y0 lose ~9 significant digits in float64: the cephes p1evl denominators drop their implied leading 1 functional claude-opus-5 https://github.com/pytorch/pytorch/issues/198583  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch-special-bessel-y0;torch-special-bessel-j1;torch-special-bessel-y1;torch-special-bessel-j0;torch-special-airy-ai</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">torch.special.bessel_j0 / bessel_j1 / bessel_y0 lose ~9 significant digits in float64: the Cephes p1evl denominators drop their implied leading 1</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/198583" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #198583 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch-special-logit [cpu] logit_backward and six activation backward kernels return a different gradient at nan depending on tensor length functional claude-opus-5 https://github.com/pytorch/pytorch/issues/195075  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch-special-logit</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[CPU] logit_backward and six activation backward kernels return a different gradient at NaN depending on tensor length</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/195075" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #195075 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch-maximum;torch-maximum--long torch.minimum and torch.maximum return a zero whose sign depends on the tensor length functional claude-opus-5 https://github.com/pytorch/pytorch/issues/193781  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch-maximum;torch-maximum--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">torch.minimum and torch.maximum return a zero whose sign depends on the tensor length</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/193781" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #193781 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch-trace;torch-trace--opus-4-8 `torch.trace` raises `notimplementederror` for `float16` input on cpu — no kernel registered for `half`, no documented exclusion, numpy handles it fine crash claude-opus-4-8 https://github.com/pytorch/pytorch/issues/184847  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch-trace;torch-trace--opus-4-8</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-4-8</span>
          </div>
          <div class="bug-title-text">`torch.trace` raises `NotImplementedError` for `float16` input on CPU — no kernel registered for `Half`, no documented exclusion, NumPy handles it fine</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/184847" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #184847 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="torch.unique torch.unique returns duplicate sub-tensors when the input contains nan functional claude-opus-5 https://github.com/pytorch/pytorch/issues/199057  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">torch.unique</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">torch.unique returns duplicate sub-tensors when the input contains NaN</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/199057" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #199057 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="torch.arctanh torch.arctanh under torch.compile loses all precision for small inputs (returns 0.0) functional claude-opus-5 https://github.com/pytorch/pytorch/issues/199058  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">torch.arctanh</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">torch.arctanh under torch.compile loses all precision for small inputs (returns 0.0)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/199058" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #199058 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="torch-clamp--long torch.clamp with a bound unrepresentable in the tensor dtype: eager raises, torch.compile ignores the bound functional claude-opus-5 https://github.com/pytorch/pytorch/issues/195675  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">torch-clamp--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">torch.clamp with a bound unrepresentable in the tensor dtype: eager raises, torch.compile ignores the bound</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/pytorch/pytorch/issues/195675" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #195675 ↗</a>
        </div>
      </div>
    </div>
  </div>
</details>
<details class="app-collapsible-card" id="app-tensorflow" data-app="tensorflow">
  <summary class="app-summary">
    <div class="app-summary-left">
      <svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="TensorFlow"><path d="M12 2L3 7.2V17.5L7.5 15V9.8L12 7.2L16.5 9.8V15L21 17.5V7.2L12 2Z" fill="#FF6F00"/><path d="M10 10.5V22L14 22V10.5L12 9.3L10 10.5Z" fill="#FFA000"/></svg>
      <span class="app-name-text">TensorFlow</span>
      <span class="app-domain-pill">Deep Learning</span>
      <span class="app-count-badge">61 bugs</span>
    </div>
    <div class="app-summary-right">
      <div class="app-pills-row">
        <span class="mini-status-pill mini-confirmed">39 Confirmed</span>
        <span class="mini-status-pill mini-fixed">10 Fixed</span>
        <span class="mini-status-pill mini-pending">4 Pending</span>
        <span class="mini-status-pill mini-rejected">8 Rejected</span>
      </div>
      <span class="app-chevron-icon" aria-hidden="true">▼</span>
    </div>
  </summary>
  <div class="app-details-body">
    <div class="bugs-cards-list">
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.linalg.svd `tf.linalg.svd` crashes on cuda raising sigabrt after facing oom crash centaur https://github.com/tensorflow/tensorflow/issues/93923  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.linalg.svd</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.linalg.svd` crashes on CUDA raising SIGABRT after facing OOM</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/93923" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #93923 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.experimental.numpy.cumsum `tf.experimental.numpy.cumsum` handles overflow inconsistently on cpu and gpu inconsistent centaur https://github.com/tensorflow/tensorflow/issues/97042 https://github.com/tensorflow/tensorflow/pull/97693 confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.experimental.numpy.cumsum</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.experimental.numpy.cumsum` handles overflow inconsistently on CPU and GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/97042" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #97042 ↗</a>
          <a href="https://github.com/tensorflow/tensorflow/pull/97693" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #97693 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.linalg.matrix_rank `tf.linalg.matrix_rank` produces inconsistent output on cpu vs gpu with `tol=6` inconsistent centaur https://github.com/tensorflow/tensorflow/issues/97102  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.linalg.matrix_rank</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.linalg.matrix_rank` produces inconsistent output on CPU vs GPU with `tol=6`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/97102" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #97102 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.nn.local_response_normalization `tf.nn.local_response_normalization` returns incorrect output inconsistent centaur https://github.com/tensorflow/tensorflow/issues/97105  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.nn.local_response_normalization</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.nn.local_response_normalization` returns incorrect output</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/97105" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #97105 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.pow `tf.pow` returns inconsistent value on cpu vs gpu inconsistent centaur https://github.com/tensorflow/tensorflow/issues/97125 https://github.com/tensorflow/tensorflow/pull/97131 confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.pow</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.pow` returns inconsistent value on CPU vs GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/97125" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #97125 ↗</a>
          <a href="https://github.com/tensorflow/tensorflow/pull/97131" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #97131 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.nn.depthwise_conv2d `tf.nn.depthwise_conv2d` crashes with large `strides` values when onednn is enabled crash centaur https://github.com/tensorflow/tensorflow/issues/97165 https://github.com/tensorflow/tensorflow/pull/97260 confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.nn.depthwise_conv2d</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.nn.depthwise_conv2d` crashes with large `strides` values when ONEDNN is enabled</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/97165" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #97165 ↗</a>
          <a href="https://github.com/tensorflow/tensorflow/pull/97260" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #97260 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.notequal inconsistent behavior for `tf.raw_ops.notequal` between cpu and gpu with non-broadcastable shapes inconsistent centaur https://github.com/tensorflow/tensorflow/issues/97204  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.NotEqual</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">Inconsistent behavior for `tf.raw_ops.NotEqual` between CPU and GPU with non-broadcastable shapes</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/97204" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #97204 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.linalg.eigh `tf.linalg.eigh` faces oom on cuda with 6d tensor and raises sigabrt crash centaur https://github.com/tensorflow/tensorflow/issues/97780  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.linalg.eigh</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.linalg.eigh` faces OOM on CUDA with 6D tensor and raises SIGABRT</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/97780" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #97780 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.linalg.lu_solve `tf.linalg.lu_solve` returns inconsistent output from cpu vs gpu inconsistent centaur https://github.com/tensorflow/tensorflow/issues/98345  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.linalg.lu_solve</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.linalg.lu_solve` returns inconsistent output from CPU vs GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/98345" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #98345 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.matrixdiag `tf.raw_ops.matrixdiag` crashes with `aborted (core dumped)` with a 6d tensor as input on gpu crash centaur https://github.com/tensorflow/tensorflow/issues/98349  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.MatrixDiag</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.raw_ops.MatrixDiag` crashes with `Aborted (core dumped)` with a 6D tensor as input on GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/98349" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #98349 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.linalg.pinv `tf.linalg.pinv` crashes with after raising sigabrt with a 6d tensor due to oom on cuda crash centaur https://github.com/tensorflow/tensorflow/issues/93822  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.linalg.pinv</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.linalg.pinv` crashes with after raising SIGABRT with a 6D tensor due to OOM on CUDA</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/93822" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #93822 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.quantizedconv2d `tf.raw_ops.quantizedconv2d` crashes with assertion failure instead of proper error handling crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94045  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.QuantizedConv2D</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">`tf.raw_ops.QuantizedConv2D` crashes with assertion failure instead of proper error handling</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94045" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94045 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.mfcc `tf.raw_ops.mfcc` causes segmentation fault crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94076  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.Mfcc</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">`tf.raw_ops.Mfcc` causes segmentation fault</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94076" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94076 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.conv3dbackpropinputv2 segmentation fault in `tf.raw_ops.conv3dbackpropinputv2` crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94114  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.Conv3DBackpropInputV2</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Segmentation Fault in `tf.raw_ops.Conv3DBackpropInputV2`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94114" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94114 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.maxpool segmentation fault in `tf.raw_ops.maxpool` with onednn and `nchw_vect_c` crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94115  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.MaxPool</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Segmentation Fault in `tf.raw_ops.MaxPool` with oneDNN and `NCHW_VECT_C`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94115" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94115 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.quantizeanddequantizev3 segmentation fault in `tf.raw_ops.quantizeanddequantizev3` crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94116  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.QuantizeAndDequantizeV3</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Segmentation Fault in `tf.raw_ops.QuantizeAndDequantizeV3`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94116" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94116 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.resourcesparseapplyproximaladagrad crash in `resourcesparseapplyproximaladagrad` crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94117  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.ResourceSparseApplyProximalAdagrad</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Crash in `ResourceSparseApplyProximalAdagrad`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94117" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94117 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.sparsebincount crash in `sparsebincount` due to overflow crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94118  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.SparseBincount</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Crash in `SparseBincount` due to overflow</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94118" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94118 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="tf.raw_ops.avgpool3dgrad floating point exception in `avgpool3dgrad` crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94119  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">tf.raw_ops.AvgPool3DGrad</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Floating Point Exception in `AvgPool3DGrad`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94119" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94119 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.maxpool3d fpe in onednn `maxpool3d` with invalid dimensions crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94120  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.MaxPool3D</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">FPE in oneDNN `MaxPool3D` with Invalid Dimensions</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94120" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94120 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.cropandresizegradboxes `segmentation fault` in cropandresizegradboxes crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94122  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.CropAndResizeGradBoxes</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">`Segmentation Fault` in CropAndResizeGradBoxes</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94122" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94122 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.histogramfixedwidth segmentation fault in `tf.raw_ops.histogramfixedwidth` crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94127  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.HistogramFixedWidth</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Segmentation Fault in `tf.raw_ops.HistogramFixedWidth`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94127" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94127 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.resourcesparseapplyadagradda crash in `tf.raw_ops.resourcesparseapplyadagradda` crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94130  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.ResourceSparseApplyAdagradDA</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Crash in `tf.raw_ops.ResourceSparseApplyAdagradDA`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94130" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94130 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="tf.raw_ops.resourcesparseapplymomentum segmentation fault in `tf.raw_ops.resourcesparseapplymomentum` crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94131  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">tf.raw_ops.ResourceSparseApplyMomentum</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Segmentation Fault in `tf.raw_ops.ResourceSparseApplyMomentum`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94131" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94131 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.tensorscattermin fatal crash in `tf.raw_ops.tensorscattermin` with malformed indices crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94132  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.TensorScatterMin</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Fatal crash in `tf.raw_ops.TensorScatterMin` with malformed indices</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94132" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94132 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.tensorscattermax fatal crash in `tf.raw_ops.tensorscattermax` with malformed indices crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94134  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.TensorScatterMax</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Fatal crash in `tf.raw_ops.TensorScatterMax` with malformed indices</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94134" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94134 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.sparsesegmentsumgradv2 inconsistent error handling in `tf.raw_ops.sparsesegmentsumgradv2` between cpu and gpu implementations inconsistent flashfuzz https://github.com/tensorflow/tensorflow/issues/94151  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.SparseSegmentSumGradV2</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Inconsistent Error Handling in `tf.raw_ops.SparseSegmentSumGradV2` Between CPU and GPU Implementations</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94151" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94151 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="tf.raw_ops.sparsetodense inconsistent error handling in `tf.raw_ops.sparsetodense` between cpu and gpu implementations inconsistent flashfuzz https://github.com/tensorflow/tensorflow/issues/94378  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">tf.raw_ops.SparseToDense</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Inconsistent Error Handling in `tf.raw_ops.SparseToDense` Between CPU and GPU Implementations</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94378" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94378 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.biasadd crash in `tf.raw_ops.biasadd` when executing on gpu crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94379  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.BiasAdd</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Crash in `tf.raw_ops.BiasAdd` when executing on GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94379" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94379 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="tf.raw_ops.maxpoolgradgradwithargmax crash in `tf.raw_ops.maxpoolgradgradwithargmax` when executing on gpu crash flashfuzz https://github.com/tensorflow/tensorflow/issues/94382  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">tf.raw_ops.MaxPoolGradGradWithArgmax</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Crash in `tf.raw_ops.MaxPoolGradGradWithArgmax` when executing on GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94382" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94382 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.conv2d_backprop_filter_v2 `tf.conv2d_backprop_filter_v2` fails with &quot;no registered kernels&quot; error internal exception flashfuzz https://github.com/tensorflow/tensorflow/issues/93903  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.conv2d_backprop_filter_v2</span>
            <span class="bug-type-pill">Internal Exception</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">`tf.conv2d_backprop_filter_v2` Fails with &quot;no registered kernels&quot; Error</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/93903" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #93903 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.linalg.triangular_solve significant discrepancy in `tf.linalg.triangular_solve` results between cpu and gpu inconsistent greyfox https://github.com/tensorflow/tensorflow/issues/79090  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.linalg.triangular_solve</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">Significant Discrepancy in `tf.linalg.triangular_solve` Results Between CPU and GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/79090" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #79090 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.linalg.lstsq `tf.linalg.lstsq` producing outputs with large inconsistencies between cpu and gpu with `float32` tensors inconsistent greyfox https://github.com/tensorflow/tensorflow/issues/79157  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.linalg.lstsq</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">`tf.linalg.lstsq` producing outputs with large inconsistencies between CPU and GPU with `float32` tensors</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/79157" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #79157 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.math.floormod `tf.math.floormod` not throwing `integer division by zero` error on gpu for tensor of int64 dtype inconsistent greyfox https://github.com/tensorflow/tensorflow/issues/79162  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.math.floormod</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">`tf.math.floormod` not throwing `Integer division by zero` error on GPU for tensor of int64 dtype</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/79162" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #79162 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.cast, tf.experimental.numpy.ascontiguousarray, tf.experimental.numpy.array, tf.saturate_cast, tf.image.convert_image_dtype inconsistency (cpu vs. gpu) when casting nan to int32 across multiple apis inconsistent rbf https://github.com/tensorflow/tensorflow/issues/106175  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.cast, tf.experimental.numpy.ascontiguousarray, tf.experimental.numpy.array, tf.saturate_cast, tf.image.convert_image_dtype</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">Inconsistency (CPU vs. GPU) when casting NaN to int32 across multiple APIs</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/106175" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #106175 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.math.unsorted_segment_max `tf.math.unsorted_segment_max` fails to propagate nans on gpu (inconsistent with cpu) inconsistent rbf https://github.com/tensorflow/tensorflow/issues/106602  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.math.unsorted_segment_max</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`tf.math.unsorted_segment_max` fails to propagate NaNs on GPU (inconsistent with CPU)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/106602" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #106602 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.eye `tf.eye` with `tf_enable_onednn_opts=1` causes crash (aborted/segfault) on large `num_columns` instead of oom crash rbf https://github.com/tensorflow/tensorflow/issues/108621  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.eye</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`tf.eye` with `TF_ENABLE_ONEDNN_OPTS=1` causes crash (Aborted/SegFault) on large `num_columns` instead of OOM</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108621" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108621 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.parallelconcat `tf.raw_ops.parallelconcat` crashes (`sigabrt`) due to integer overflow in shape calculation crash rbf https://github.com/tensorflow/tensorflow/issues/108663  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.ParallelConcat</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`tf.raw_ops.ParallelConcat` crashes (`SIGABRT`) due to integer overflow in shape calculation</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108663" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108663 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="tf.raw_ops.audiospectrogram `tf.raw_ops.audiospectrogram` segfaults with negative `window_size` and `stride` crash rbf https://github.com/tensorflow/tensorflow/issues/108664 https://github.com/tensorflow/tensorflow/pull/109326 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">tf.raw_ops.AudioSpectrogram</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`tf.raw_ops.AudioSpectrogram` Segfaults with negative `window_size` and `stride`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108664" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108664 ↗</a>
          <a href="https://github.com/tensorflow/tensorflow/pull/109326" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #109326 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.raw_ops.immutableconst `tf.raw_ops.immutableconst` causes segfault (`sigsegv`) with large shape dimensions crash rbf https://github.com/tensorflow/tensorflow/issues/108665 https://github.com/tensorflow/tensorflow/pull/108705 confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.raw_ops.ImmutableConst</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`tf.raw_ops.ImmutableConst` causes Segfault (`SIGSEGV`) with large shape dimensions</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108665" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108665 ↗</a>
          <a href="https://github.com/tensorflow/tensorflow/pull/108705" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #108705 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.experimental.numpy.amax `tf.experimental.numpy.amax` crashes (`sigabrt`) with specific int64 overflow in shape crash rbf https://github.com/tensorflow/tensorflow/issues/108891  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.experimental.numpy.amax</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`tf.experimental.numpy.amax` crashes (`SIGABRT`) with specific int64 overflow in shape</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108891" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108891 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="tf.io.encode_png `tf.io.encode_png` crashes process (`sigabrt`) with `check` failure when input has 0-dimension crash rbf https://github.com/tensorflow/tensorflow/issues/108916 https://github.com/tensorflow/tensorflow/pull/109131 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">tf.io.encode_png</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`tf.io.encode_png` crashes process (`SIGABRT`) with `CHECK` failure when input has 0-dimension</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108916" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108916 ↗</a>
          <a href="https://github.com/tensorflow/tensorflow/pull/109131" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #109131 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.linalg.det,tf.linalg.slogdet,tf.linalg.logdet,tf.linalg.cholesky,tf.linalg.inv aborted (core dumped) in `tf.linalg.det/slogdet/logdet/cholesky/inv` crash rbf https://github.com/tensorflow/tensorflow/issues/76730  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.linalg.det,tf.linalg.slogdet,tf.linalg.logdet,tf.linalg.cholesky,tf.linalg.inv</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">Aborted (core dumped) in `tf.linalg.det/slogdet/logdet/cholesky/inv`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/76730" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #76730 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="tf.histogram_fixed_width segmentation fault when tf.histogram_fixed_width receives large `value_range` and `nbins` on cpu mode crash rbf https://github.com/tensorflow/tensorflow/issues/68836  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">tf.histogram_fixed_width</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">segmentation fault when tf.histogram_fixed_width receives large `value_range` and `nbins` on CPU mode</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/68836" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #68836 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="tf.math.argmax,tf.experimental.numpy.argmax `tf.math.argmax` throws `invalidargumenterror` with valid `axis` of `int16` dtype false positive centaur https://github.com/tensorflow/tensorflow/issues/97096  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">tf.math.argmax,tf.experimental.numpy.argmax</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.math.argmax` throws `InvalidArgumentError` with valid `axis` of `int16` dtype</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/97096" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #97096 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="tf.raw_ops.sparsesegmentsqrtngradv2 inconsistent error handling in `tf.raw_ops.sparsesegmentsqrtngradv2` between cpu and gpu implementations inconsistent flashfuzz https://github.com/tensorflow/tensorflow/issues/94376  fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">tf.raw_ops.SparseSegmentSqrtNGradV2</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Inconsistent Error Handling in `tf.raw_ops.SparseSegmentSqrtNGradV2` Between CPU and GPU Implementations</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/94376" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #94376 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="tf.nn.conv2d_transpose `tf.nn.conv2d_transpose` crashes with &quot;illegal instruction (core dumped)&quot; crash centaur https://github.com/tensorflow/tensorflow/issues/93733  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">tf.nn.conv2d_transpose</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">Centaur</span>
          </div>
          <div class="bug-title-text">`tf.nn.conv2d_transpose` crashes with &quot;Illegal instruction (core dumped)&quot;</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/93733" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #93733 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="tf.math.pow inconsistent results between cpu and gpu for `tf.math.pow` false positive greyfox https://github.com/tensorflow/tensorflow/issues/79060  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">tf.math.pow</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">Inconsistent Results Between CPU and GPU for `tf.math.pow`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/79060" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #79060 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="tf.experimental.numpy.nansum discrepancy in `tf.experimental.numpy.nansum` with `dtype=float16` on cpu vs gpu false positive greyfox https://github.com/tensorflow/tensorflow/issues/79083  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">tf.experimental.numpy.nansum</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">Discrepancy in `tf.experimental.numpy.nansum` with `dtype=float16` on CPU vs GPU</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/79083" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #79083 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="tf.compat.as_str_any misleading output when an invalid encoding parameter passed to tf.compat.as_str_any false positive rbf https://github.com/tensorflow/tensorflow/issues/108548  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">tf.compat.as_str_any</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">Misleading output when an invalid encoding Parameter Passed to tf.compat.as_str_any</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108548" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108548 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="tf.compat.dimension_value tf.compat.dimension_value returns a tensor when given a tensor, despite documentation stating it returns only int or none. false positive rbf https://github.com/tensorflow/tensorflow/issues/108605  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">tf.compat.dimension_value</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">tf.compat.dimension_value returns a Tensor when given a Tensor, despite documentation stating it returns only int or None.</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108605" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108605 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="tf.compat.forward_compatible tf.compat.forward_compatible does not validate year/month/day ranges as documented false positive rbf https://github.com/tensorflow/tensorflow/issues/108608  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">tf.compat.forward_compatible</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">tf.compat.forward_compatible does not validate year/month/day ranges as documented</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108608" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108608 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="tf.concat when a single tensor and out of range axis is passed to tf.concat it silently succeeds false positive rbf https://github.com/tensorflow/tensorflow/issues/108628  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">tf.concat</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">When a single tensor and out of range axis is passed to tf.concat it silently succeeds</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108628" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108628 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="tf.experimental.numpy.asarray cpu/gpu inconsistency when casting bfloat16 to int8 for the api tf.experimental.numpy.asarray false positive rbf https://github.com/tensorflow/tensorflow/issues/108629  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">tf.experimental.numpy.asarray</span>
            <span class="bug-type-pill">False positive</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">CPU/GPU inconsistency when casting bfloat16 to int8 for the api tf.experimental.numpy.asarray</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108629" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108629 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Fixed" data-search="tf.raw_ops.quantizedmaxpool unclear error message in tf.raw_ops.quantizedmaxpool with onednn enabled internal exception flashfuzz https://github.com/tensorflow/tensorflow/issues/100223 https://github.com/tensorflow/tensorflow/pull/122516 fixed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-fixed"><span class="status-dot dot-fixed"></span>Fixed</span>
            <span class="bug-api-code">tf.raw_ops.QuantizedMaxPool</span>
            <span class="bug-type-pill">Internal Exception</span>
            <span class="bug-tool-pill">Flashfuzz</span>
          </div>
          <div class="bug-title-text">Unclear Error Message in tf.raw_ops.QuantizedMaxPool with oneDNN Enabled</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/100223" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #100223 ↗</a>
          <a href="https://github.com/tensorflow/tensorflow/pull/122516" target="_blank" rel="noopener noreferrer" class="bug-pr-btn" title="View associated Pull Request">PR #122516 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.gather discrepancy in error handling for `tf.gather` on cpu vs gpu leading to undefined behavior inconsistent greyfox https://github.com/tensorflow/tensorflow/issues/79063  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.gather</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">Greyfox</span>
          </div>
          <div class="bug-title-text">Discrepancy in Error Handling for `tf.gather` on CPU vs GPU Leading to Undefined Behavior</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/79063" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #79063 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="tf.raw_ops.sparsefillemptyrowsgrad tf.raw_ops.sparsefillemptyrowsgrad cpu-gpu inconsistency for out-of-range reverse_index_map inconsistent rbf https://github.com/tensorflow/tensorflow/issues/106388  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">tf.raw_ops.SparseFillEmptyRowsGrad</span>
            <span class="bug-type-pill">Inconsistent</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">tf.raw_ops.SparseFillEmptyRowsGrad CPU-GPU inconsistency for out-of-range reverse_index_map</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/106388" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #106388 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="tf.experimental.numpy.ones, tf.experimental.numpy.zeros `tf.experimental.numpy.ones` crashes (segfault/abort) when int64_max is passed as shape crash rbf https://github.com/tensorflow/tensorflow/issues/108904  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">tf.experimental.numpy.ones, tf.experimental.numpy.zeros</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`tf.experimental.numpy.ones` crashes (segfault/abort) when INT64_MAX is passed as shape</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108904" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108904 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="tf.experimental.numpy.var, tf.experimental.numpy.all, tf.experimental.numpy.any, tf.experimental.numpy.amax, tf.experimental.numpy.amin, tf.experimental.numpy.count_nonzero, tf.experimental.numpy.max, tf.experimental.numpy.nanmean, tf.experimental.numpy.ptp, tf.experimental.numpy.nansum, tf.experimental.numpy.reshape, tf.experimental.numpy.promote_types, tf.experimental.numpy.var, tf.experimental.numpy.std `tf.experimental.numpy.var` causes `sigabrt` on empty tensors with large dimensions crash rbf https://github.com/tensorflow/tensorflow/issues/108921  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">tf.experimental.numpy.var, tf.experimental.numpy.all, tf.experimental.numpy.any, tf.experimental.numpy.amax, tf.experimental.numpy.amin, tf.experimental.numpy.count_nonzero, tf.experimental.numpy.max, tf.experimental.numpy.nanmean, tf.experimental.numpy.ptp, tf.experimental.numpy.nansum, tf.experimental.numpy.reshape, tf.experimental.numpy.promote_types, tf.experimental.numpy.var, tf.experimental.numpy.std</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`tf.experimental.numpy.var` Causes `SIGABRT` on Empty Tensors with Large Dimensions</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/108921" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #108921 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="tf.math.reduce_variance `tf.math.reduce_variance` causes `sigabrt` on large shapes containing zero crash rbf https://github.com/tensorflow/tensorflow/issues/109148  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">tf.math.reduce_variance</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`tf.math.reduce_variance` causes `SIGABRT` on large shapes containing zero</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/109148" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #109148 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="tf.image.non_max_suppression `tf.image.non_max_suppression` causes `sigabrt` (check failure) with negative `max_output_size` crash rbf https://github.com/tensorflow/tensorflow/issues/109150  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">tf.image.non_max_suppression</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">RBF</span>
          </div>
          <div class="bug-title-text">`tf.image.non_max_suppression` causes `SIGABRT` (Check Failure) with negative `max_output_size`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/tensorflow/tensorflow/issues/109150" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #109150 ↗</a>
        </div>
      </div>
    </div>
  </div>
</details>
<details class="app-collapsible-card" id="app-jax" data-app="jax">
  <summary class="app-summary">
    <div class="app-summary-left">
      <svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="JAX"><rect x="2" y="4" width="20" height="16" rx="4" fill="#E8F0FE"/><text x="12" y="15.5" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="800" fill="#1A73E8" text-anchor="middle" letter-spacing="-0.02em">JAX</text></svg>
      <span class="app-name-text">JAX</span>
      <span class="app-domain-pill">Autodiff / ML</span>
      <span class="app-count-badge">38 bugs</span>
    </div>
    <div class="app-summary-right">
      <div class="app-pills-row">
        <span class="mini-status-pill mini-confirmed">28 Confirmed</span>
        <span class="mini-status-pill mini-pending">9 Pending</span>
        <span class="mini-status-pill mini-rejected">1 Rejected</span>
      </div>
      <span class="app-chevron-icon" aria-hidden="true">▼</span>
    </div>
  </summary>
  <div class="app-details-body">
    <div class="bugs-cards-list">
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-betaln;jax-scipy-special-beta;jax-scipy-special-betaln--again;jax-scipy-special-beta--again;jax-scipy-special-betaln--long;jax-scipy-special-beta--long betaln(a, b) is too large by exactly min(a, b) when min(a, b)/max(a, b) is subnormal functional claude-opus-5 https://github.com/jax-ml/jax/issues/40653  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-betaln;jax-scipy-special-beta;jax-scipy-special-betaln--again;jax-scipy-special-beta--again;jax-scipy-special-betaln--long;jax-scipy-special-beta--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">betaln(a, b) is too large by exactly min(a, b) when min(a, b)/max(a, b) is subnormal</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/40653" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #40653 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="jax-numpy-histogram jnp.histogram assigns values lying exactly on an interior bin edge to the wrong bin functional claude-opus-5 https://github.com/jax-ml/jax/issues/40963  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">jax-numpy-histogram</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jnp.histogram assigns values lying exactly on an interior bin edge to the wrong bin</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/40963" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #40963 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-stats-pareto jax.scipy.stats.pareto returns -inf/inf/nan at the support boundary when scale is small relative to loc (support mask computed on unstandardized x) functional claude-opus-5 https://github.com/jax-ml/jax/issues/40964  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-stats-pareto</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.pareto returns -inf/inf/nan at the support boundary when scale is small relative to loc (support mask computed on unstandardized x)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/40964" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #40964 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-stats-expon jax.scipy.stats.expon.logcdf returns -inf for small positive x (log1p(-sf) cancellation) functional claude-opus-5 https://github.com/jax-ml/jax/issues/40965  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-stats-expon</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.expon.logcdf returns -inf for small positive x (log1p(-sf) cancellation)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/40965" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #40965 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-stats-laplace jax.scipy.stats.laplace.cdf gives nan gradients in the tails (unselected branch overflows) functional claude-opus-5 https://github.com/jax-ml/jax/issues/40966  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-stats-laplace</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.laplace.cdf gives NaN gradients in the tails (unselected branch overflows)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/40966" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #40966 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-jit jax.jit: negative static_argnums is not applied when the argument is passed by keyword (static_argnames not inferred) functional claude-opus-5 https://github.com/jax-ml/jax/issues/40967  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-jit</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.jit: negative static_argnums is not applied when the argument is passed by keyword (static_argnames not inferred)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/40967" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #40967 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-zeta;jax-scipy-special-zeta--long jax.scipy.special.zeta: the custom_jvp rule returns a different primal value than the function (nan vs finite for s &lt; 1) functional claude-opus-5 https://github.com/jax-ml/jax/issues/40968  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-zeta;jax-scipy-special-zeta--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.zeta: the custom_jvp rule returns a different primal value than the function (nan vs finite for s &lt; 1)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/40968" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #40968 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-stats-poisson;jax-scipy-stats-poisson--long jax.scipy.stats.poisson.entropy returns nan gradients for large mu (and small mu in float32) functional claude-opus-5 https://github.com/jax-ml/jax/issues/40969  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-stats-poisson;jax-scipy-stats-poisson--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.poisson.entropy returns NaN gradients for large mu (and small mu in float32)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/40969" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #40969 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-betaln jax.scipy.special.beta returns nan / wrong sign at multiple defined points (negative integers, ±inf, -0) functional claude-opus-5 https://github.com/jax-ml/jax/issues/38270  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-betaln</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.beta returns nan / wrong sign at multiple defined points (negative integers, ±inf, -0)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38270" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38270 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-i0;jax-scipy-special-i1 jax.scipy.special.i1 overflows to inf for large finite float64 input functional claude-opus-5 https://github.com/jax-ml/jax/issues/39772  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-i0;jax-scipy-special-i1</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.i1 overflows to inf for large finite float64 input</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/39772" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #39772 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-stats-uniform jax.scipy.stats.uniform.cdf/pdf/logpdf silently map nan input to finite values (pdf(nan) == 1.0) functional claude-opus-5 https://github.com/jax-ml/jax/issues/38317  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-stats-uniform</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.uniform.cdf/pdf/logpdf silently map NaN input to finite values (pdf(nan) == 1.0)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38317" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38317 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-stats-vonmises jax.scipy.stats.vonmises.pdf returns nan at kappa=0.0 functional claude-opus-5 https://github.com/jax-ml/jax/issues/38621  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-stats-vonmises</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.vonmises.pdf returns nan at kappa=0.0</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38621" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38621 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="jax-scipy-special-rel-entr jax.scipy.special.rel_entr(0.0, nan) returns inf instead of nan — scipy compatibility mismatch functional claude-opus-5 https://github.com/jax-ml/jax/issues/38262  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">jax-scipy-special-rel-entr</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.rel_entr(0.0, nan) returns inf instead of nan — SciPy compatibility mismatch</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38262" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38262 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-kl-div jax.scipy.special.kl_div returns nan instead of inf at x=inf, y=0.0 functional claude-opus-5 https://github.com/jax-ml/jax/issues/38239  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-kl-div</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.kl_div returns nan instead of inf at x=inf, y=0.0</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38239" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38239 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-stats-cauchy jax.scipy.stats.cauchy.ppf/isf: no quantile-domain handling — ppf(0) returns large finite value (wrong sign in float32), q outside [0,1] returns garbage functional claude-opus-5 https://github.com/jax-ml/jax/issues/38318  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-stats-cauchy</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.cauchy.ppf/isf: no quantile-domain handling — ppf(0) returns large finite value (wrong sign in float32), q outside [0,1] returns garbage</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38318" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38318 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-stats-chi2 jax.scipy.stats.chi2.logpdf returns nan at x=0 and x=inf when df=2 (inconsistent with gamma.logpdf) functional claude-opus-5 https://github.com/jax-ml/jax/issues/38316  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-stats-chi2</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.chi2.logpdf returns NaN at x=0 and x=inf when df=2 (inconsistent with gamma.logpdf)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38316" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38316 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-stats-dirichlet jax.scipy.stats.dirichlet.logpdf returns -inf at simplex boundary where density diverges to +inf (alpha&lt;1) functional claude-opus-5 https://github.com/jax-ml/jax/issues/38520  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-stats-dirichlet</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.dirichlet.logpdf returns -inf at simplex boundary where density diverges to +inf (alpha&lt;1)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38520" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38520 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-stats-multinomial jax.scipy.stats.multinomial.logpmf/pmf return -inf for all rows of a batched input (sum reduces over all axes, not axis=-1) functional claude-opus-5 https://github.com/jax-ml/jax/issues/38605  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-stats-multinomial</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.multinomial.logpmf/pmf return -inf for all rows of a batched input (sum reduces over all axes, not axis=-1)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38605" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38605 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-erfcx jax.scipy.special.erfcx returns spurious 0.0 in a band near x≈26.6 (should be ~0.0212; scipy/torch agree) functional claude-opus-5 https://github.com/jax-ml/jax/issues/38607  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-erfcx</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.erfcx returns spurious 0.0 in a band near x≈26.6 (should be ~0.0212; scipy/torch agree)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38607" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38607 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-xlog1py;jax-scipy-special-xlogy;jax-scipy-special-xlogy--opus-4-8 `jax.scipy.special.xlogy` and `xlog1py` return `0.0` instead of `nan` when `x=0` and `y=nan` functional claude-opus-4-8 https://github.com/jax-ml/jax/issues/37751  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-xlog1py;jax-scipy-special-xlogy;jax-scipy-special-xlogy--opus-4-8</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-4-8</span>
          </div>
          <div class="bug-title-text">`jax.scipy.special.xlogy` and `xlog1py` return `0.0` instead of `nan` when `x=0` and `y=nan`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/37751" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #37751 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-numpy-abs;jax-numpy-abs--opus-4-8 `jnp.abs(inf + nan*j)` returns `nan` — violates ieee 754 / c99 &quot;infinity dominates&quot; rule for complex magnitude functional claude-opus-4-8 https://github.com/jax-ml/jax/issues/37817  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-numpy-abs;jax-numpy-abs--opus-4-8</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-4-8</span>
          </div>
          <div class="bug-title-text">`jnp.abs(inf + nan*j)` returns `nan` — violates IEEE 754 / C99 &quot;infinity dominates&quot; rule for complex magnitude</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/37817" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #37817 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-digamma--opus-4-8 `jax.scipy.special.digamma(0.0)` returns `nan` — should be `-inf` functional claude-opus-4-8 https://github.com/jax-ml/jax/issues/37763  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-digamma--opus-4-8</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-4-8</span>
          </div>
          <div class="bug-title-text">`jax.scipy.special.digamma(0.0)` returns `nan` — should be `-inf`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/37763" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #37763 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-loggamma--again jax.scipy.special.loggamma returns nan instead of inf at x=0.0 and x=-0.0 functional claude-opus-5 https://github.com/jax-ml/jax/issues/38240  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-loggamma--again</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.loggamma returns nan instead of inf at x=0.0 and x=-0.0</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38240" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38240 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-zeta--again jax.lax.zeta gives wrong results for negative non-integer q (euler-maclaurin breakdown) functional claude-opus-5 https://github.com/jax-ml/jax/issues/38199  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-zeta--again</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.lax.zeta gives wrong results for negative non-integer q (Euler-Maclaurin breakdown)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38199" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38199 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax.array.sum jax.array.sum silently ignores the `initial` argument functional claude-opus-5 https://github.com/jax-ml/jax/issues/41120  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax.Array.sum</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.Array.sum silently ignores the `initial` argument</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41120" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41120 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax.fwd_and_bwd jax.fwd_and_bwd silently discards keyword arguments functional claude-opus-5 https://github.com/jax-ml/jax/issues/41121  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax.fwd_and_bwd</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.fwd_and_bwd silently discards keyword arguments</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41121" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41121 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="jax.lax.pmean `lax.pmean` with unequal `axis_index_groups` divides every group by the size of the first group functional claude-opus-5 https://github.com/jax-ml/jax/issues/41132  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">jax.lax.pmean</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`lax.pmean` with unequal `axis_index_groups` divides every group by the size of the first group</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41132" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41132 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-gammaln--long jax.scipy.special.gammaln(-inf) returns +inf instead of -inf — sign-wrong at infinity edge functional claude-opus-5 https://github.com/jax-ml/jax/issues/38264  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-gammaln--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.gammaln(-inf) returns +inf instead of -inf — sign-wrong at infinity edge</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/38264" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #38264 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-rel-entr;jax-scipy-special-kl-div;jax-scipy-special-kl-div--long jax.scipy.special.rel_entr / kl_div lose all precision for p close to q and return nan for large p (p*log(p) - p*log(q)) functional claude-opus-5 https://github.com/jax-ml/jax/issues/41200  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-rel-entr;jax-scipy-special-kl-div;jax-scipy-special-kl-div--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.rel_entr / kl_div lose all precision for p close to q and return nan for large p (p*log(p) - p*log(q))</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41200" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41200 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="jax-scipy-special-gammaincc;jax-scipy-special-gammaincc--long jax.scipy.special.gammaincc returns values far outside [0, 1] for large a (continued fraction stops unconverged) functional claude-opus-5 https://github.com/jax-ml/jax/issues/41201  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">jax-scipy-special-gammaincc;jax-scipy-special-gammaincc--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.gammaincc returns values far outside [0, 1] for large a (continued fraction stops unconverged)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41201" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41201 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="jax-random-poisson jax.random.poisson: samples for large lam (&gt;~2e5) have the wrong variance (+46% at lam=1e8) functional claude-opus-5 https://github.com/jax-ml/jax/issues/41202  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">jax-random-poisson</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.random.poisson: samples for large lam (&gt;~2e5) have the wrong variance (+46% at lam=1e8)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41202" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41202 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="jax-scipy-stats-t jax.scipy.stats.t.logpdf is wrong for large df (lgamma(df/2) - lgamma((df+1)/2) cancels): logpdf(0, df=1e7) = 0 in float32 functional claude-opus-5 https://github.com/jax-ml/jax/issues/41203  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">jax-scipy-stats-t</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.t.logpdf is wrong for large df (lgamma(df/2) - lgamma((df+1)/2) cancels): logpdf(0, df=1e7) = 0 in float32</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41203" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41203 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-numpy-linalg-eigh jnp.linalg.eigh silently accepts (…, 1, n) / (…, n, 1) input and returns the decomposition of a broadcast n x n matrix functional claude-opus-5 https://github.com/jax-ml/jax/issues/41204  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-numpy-linalg-eigh</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jnp.linalg.eigh silently accepts (…, 1, n) / (…, n, 1) input and returns the decomposition of a broadcast n x n matrix</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41204" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41204 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="jax-scipy-special-expn jax.scipy.special.expn(n, 0) returns 1/n instead of 1/(n-1) for n &gt;= 2 functional claude-opus-5 https://github.com/jax-ml/jax/issues/41205  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">jax-scipy-special-expn</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.expn(n, 0) returns 1/n instead of 1/(n-1) for n &gt;= 2</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41205" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41205 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="jax-numpy-floor-divide;jax-numpy-floor-divide--long jnp.floor_divide / divmod return a quotient larger than x1/x2 for some float16 and bfloat16 inputs functional claude-opus-5 https://github.com/jax-ml/jax/issues/41206  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">jax-numpy-floor-divide;jax-numpy-floor-divide--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jnp.floor_divide / divmod return a quotient larger than x1/x2 for some float16 and bfloat16 inputs</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41206" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41206 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="jax-scipy-special-expi--again;jax-scipy-special-expi--long jax.scipy.special.expi(0.0)` returns nan instead of -inf functional claude-opus-5 https://github.com/jax-ml/jax/issues/41207  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">jax-scipy-special-expi--again;jax-scipy-special-expi--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.special.expi(0.0)` returns nan instead of -inf</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41207" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41207 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="jax-scipy-stats-poisson--again jax.scipy.stats.poisson.logpmf` applies the integrality test to `k` instead of `k - loc` functional claude-opus-5 https://github.com/jax-ml/jax/issues/41208  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">jax-scipy-stats-poisson--again</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jax.scipy.stats.poisson.logpmf` applies the integrality test to `k` instead of `k - loc`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41208" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41208 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="jax#1;jax_1 `jnp.add.reduceat` and `jnp.multiply.reduceat` ignore the requested accumulator dtype functional claude-opus-5 https://github.com/jax-ml/jax/issues/41246  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">jax#1;jax_1</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`jnp.add.reduceat` and `jnp.multiply.reduceat` ignore the requested accumulator dtype</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/jax-ml/jax/issues/41246" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41246 ↗</a>
        </div>
      </div>
    </div>
  </div>
</details>
<details class="app-collapsible-card" id="app-vllm" data-app="vllm">
  <summary class="app-summary">
    <div class="app-summary-left">
      <svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="vLLM"><path d="M4 4L12 20L20 4H15.5L12 13L8.5 4H4Z" fill="#2563EB"/><circle cx="12" cy="7" r="2.2" fill="#60A5FA"/></svg>
      <span class="app-name-text">vLLM</span>
      <span class="app-domain-pill">LLM Serving</span>
      <span class="app-count-badge">34 bugs</span>
    </div>
    <div class="app-summary-right">
      <div class="app-pills-row">
        <span class="mini-status-pill mini-confirmed">27 Confirmed</span>
        <span class="mini-status-pill mini-pending">7 Pending</span>
      </div>
      <span class="app-chevron-icon" aria-hidden="true">▼</span>
    </div>
  </summary>
  <div class="app-details-body">
    <div class="bugs-cards-list">
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-tool-parsers-gigachat3-tool-parser [bug]: gigachat3, granite and granite-20b-fc tool parsers lose tool calls when the whole message arrives in a single streaming delta functional claude-opus-5 https://github.com/vllm-project/vllm/issues/47907  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-tool-parsers-gigachat3-tool-parser</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: gigachat3, granite and granite-20b-fc tool parsers lose tool calls when the whole message arrives in a single streaming delta</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/47907" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #47907 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="vllm-reasoning-olmo3-reasoning-parser;vllm-reasoning-deepseek-r1-reasoning-parser;vllm-reasoning-ernie45-reasoning-parser;vllm-parser-abstract-parser [bug]: reasoning parsers mishandle markers in multi-token streaming deltas functional claude-opus-5 https://github.com/vllm-project/vllm/issues/55195  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">vllm-reasoning-olmo3-reasoning-parser;vllm-reasoning-deepseek-r1-reasoning-parser;vllm-reasoning-ernie45-reasoning-parser;vllm-parser-abstract-parser</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: Reasoning parsers mishandle markers in multi-token streaming deltas</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/55195" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #55195 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-tokenizers-detokenizer-utils fix(logprobs): guard convert_ids_list_to_tokens against out-of-range ids crash claude-opus-5 https://github.com/vllm-project/vllm/pull/48567  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-tokenizers-detokenizer-utils</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">fix(logprobs): guard convert_ids_list_to_tokens against out-of-range ids</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/48567" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #48567 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-utils-argparse-utils [bugfix] parse human-readable ints with decimal to avoid off-by-one functional claude-opus-5 https://github.com/vllm-project/vllm/pull/58333  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-utils-argparse-utils</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Parse human-readable ints with Decimal to avoid off-by-one</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/58333" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #58333 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-utils-argparse-utils [bugfix] avoid an indexerror for trailing dotted cli args crash claude-opus-5 https://github.com/vllm-project/vllm/pull/54587  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-utils-argparse-utils</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Avoid an IndexError for trailing dotted CLI args</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/54587" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #54587 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-reasoning-olmo3-reasoning-parser [bugfix][reasoning] olmo3: keep literal think tags in streamed content functional claude-opus-5 https://github.com/vllm-project/vllm/pull/48971  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-reasoning-olmo3-reasoning-parser</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix][Reasoning] Olmo3: keep literal think tags in streamed content</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/48971" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #48971 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-engine-arg-utils-engineargs;vllm-engine-arg-utils-engineargs--reported;vllm-engine-arg-utils-engineargs--gpu;vllm-engine-arg-utils-engineargs--long [bugfix] let an optional literal flag accept the none it advertises functional claude-opus-5 https://github.com/vllm-project/vllm/pull/52370  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-engine-arg-utils-engineargs;vllm-engine-arg-utils-engineargs--reported;vllm-engine-arg-utils-engineargs--gpu;vllm-engine-arg-utils-engineargs--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Let an optional Literal flag accept the None it advertises</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/52370" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #52370 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-tool-parsers-internlm2-tool-parser;vllm-tool-parsers-internlm2-tool-parser--long [bugfix][tool parser] return early for unlisted tool names in internlm2 parser functional claude-opus-5 https://github.com/vllm-project/vllm/pull/47968  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-tool-parsers-internlm2-tool-parser;vllm-tool-parsers-internlm2-tool-parser--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix][Tool Parser] Return early for unlisted tool names in InternLM2 parser</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/47968" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #47968 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-utils-collection-utils [bugfix] invalidate lazydict cache on __setitem__ functional claude-opus-5 https://github.com/vllm-project/vllm/pull/52541  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-utils-collection-utils</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Invalidate LazyDict cache on __setitem__</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/52541" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #52541 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-utils-collection-utils [bugfix][core] preserve none values in swap_dict_values functional claude-opus-5 https://github.com/vllm-project/vllm/pull/47961  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-utils-collection-utils</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix][Core] Preserve None values in swap_dict_values</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/47961" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #47961 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-tool-parsers-utils [bugfix] fix extreme case in pythonic parser argument json safety functional claude-opus-5 https://github.com/vllm-project/vllm/pull/51649  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-tool-parsers-utils</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Fix extreme case in pythonic parser argument json safety</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/51649" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #51649 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-sampling-params-structuredoutputsparams [bugfix][structured outputs] reject empty `structural_tag` at request validation crash claude-opus-5 https://github.com/vllm-project/vllm/pull/47450  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-sampling-params-structuredoutputsparams</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix][Structured Outputs] Reject empty `structural_tag` at request validation</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/47450" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #47450 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-tool-parsers-xlam-tool-parser;vllm-tool-parsers-hunyuan-a13b-tool-parser [bug]: xlam and hunyuan_a13b tool parsers drop the arguments of any tool call that follows an empty-argument call (streaming) functional claude-opus-5 https://github.com/vllm-project/vllm/issues/47901  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-tool-parsers-xlam-tool-parser;vllm-tool-parsers-hunyuan-a13b-tool-parser</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: xlam and hunyuan_a13b tool parsers drop the arguments of any tool call that follows an empty-argument call (streaming)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/47901" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #47901 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-reasoning-basic-parsers [bugfix] count reasoning tokens when the start token is absent functional claude-opus-5 https://github.com/vllm-project/vllm/pull/49743  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-reasoning-basic-parsers</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Count reasoning tokens when the start token is absent</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/49743" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #49743 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-entrypoints-openai-completion-protocol-completionreques [bugfix] reject empty prompt lists in completionrequest functional claude-opus-5 https://github.com/vllm-project/vllm/pull/55391  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-entrypoints-openai-completion-protocol-completionreques</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] reject empty prompt lists in CompletionRequest</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/55391" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #55391 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-entrypoints-openai-completion-protocol-completionreques [bugfix][frontend] avoid mutating openai request extra args functional claude-opus-5 https://github.com/vllm-project/vllm/pull/50353  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-entrypoints-openai-completion-protocol-completionreques</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix][Frontend] Avoid mutating OpenAI request extra args</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/50353" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #50353 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-reasoning-deepseek-v3-reasoning-parser [bugfix][frontend] count reasoning tokens for harmony, deepseek-v3 and step3 parsers functional claude-opus-5 https://github.com/vllm-project/vllm/pull/58626  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-reasoning-deepseek-v3-reasoning-parser</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix][Frontend] Count reasoning tokens for Harmony, DeepSeek-V3 and Step3 parsers</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/58626" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #58626 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-reasoning-ernie45-reasoning-parser fix(reasoning): recompute ernie45 response-end index after stripping prefix functional claude-opus-5 https://github.com/vllm-project/vllm/pull/48386  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-reasoning-ernie45-reasoning-parser</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">fix(reasoning): recompute ernie45 response-end index after stripping prefix</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/48386" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #48386 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-v1-structured-output [bugfix] escape control characters in xgrammar choice grammar functional claude-opus-5 https://github.com/vllm-project/vllm/pull/48115  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-v1-structured-output</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Escape control characters in xgrammar choice grammar</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/48115" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #48115 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-v1-structured-output [bugfix] make lark-to-ebnf quote handling escape-aware functional claude-opus-5 https://github.com/vllm-project/vllm/pull/57695  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-v1-structured-output</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Make Lark-to-EBNF quote handling escape-aware</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/57695" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #57695 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-tool-parsers-abstract-tool-parser-toolparser [bugfix] avoid mutating tool parameters in _get_tool_schema_defs functional claude-opus-5 https://github.com/vllm-project/vllm/pull/46170  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-tool-parsers-abstract-tool-parser-toolparser</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Avoid mutating tool parameters in _get_tool_schema_defs</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/46170" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #46170 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-tool-parsers-internlm2-tool-parser;vllm-tool-parsers-internlm2-tool-parser--long [bugfix] limit split to first marker in internlm2 tool parser crash claude-opus-5 https://github.com/vllm-project/vllm/pull/44163  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-tool-parsers-internlm2-tool-parser;vllm-tool-parsers-internlm2-tool-parser--long</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Limit split to first marker in internlm2 tool parser</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/44163" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #44163 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="vllm-model-executor-models-qwen3-moe [bug]: qwen3moesparsemoeblock rejects its documented 1d input functional claude-opus-5 https://github.com/vllm-project/vllm/issues/55205  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">vllm-model-executor-models-qwen3-moe</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: Qwen3MoeSparseMoeBlock rejects its documented 1D input</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/55205" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #55205 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="vllm-model-executor-layers-rotary-embedding-fope [bug]: fourierrotaryembedding pads sin with 1 and corrupts unrotated channels crash claude-opus-5 https://github.com/vllm-project/vllm/issues/55204  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">vllm-model-executor-layers-rotary-embedding-fope</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: FourierRotaryEmbedding pads sin with 1 and corrupts unrotated channels</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/55204" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #55204 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm-lora;vllm-lora--again;vllm-lora--long [bugfix][lora] skip no-lora tokens (index -1) in cpu torch bgmv ops functional claude-opus-5 https://github.com/vllm-project/vllm/pull/48421  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm-lora;vllm-lora--again;vllm-lora--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix][LoRA] Skip no-LoRA tokens (index -1) in CPU torch bgmv ops</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/pull/48421" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #48421 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="vllm.multimodal.audio.audiospec [bug]: audiospec(target_channels=1) does not produce 1d mono output for single-channel 2d audio functional claude-opus-5 https://github.com/vllm-project/vllm/issues/59267  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">vllm.multimodal.audio.AudioSpec</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: AudioSpec(target_channels=1) does not produce 1D mono output for single-channel 2D audio</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/59267" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #59267 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="vllm.utils.system_utils.suppress_stdout [bug]: vllm.utils.system_utils.suppress_stdout crashes when sys.stdout has no file descriptor crash claude-opus-5 https://github.com/vllm-project/vllm/issues/59268  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">vllm.utils.system_utils.suppress_stdout</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: vllm.utils.system_utils.suppress_stdout crashes when sys.stdout has no file descriptor</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/59268" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #59268 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="vllm.utils.system_utils.suppress_stdout [bug]: vllm.utils.system_utils.suppress_stdout silently suppresses stderr when sys.stdout is bound to fd 2 crash claude-opus-5 https://github.com/vllm-project/vllm/issues/59269  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">vllm.utils.system_utils.suppress_stdout</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: vllm.utils.system_utils.suppress_stdout silently suppresses stderr when sys.stdout is bound to fd 2</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/59269" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #59269 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="vllm.plugins.lora_resolvers.filesystem_resolver.register_filesystem_resolver [bug]: filesystemresolver loads adapters outside vllm_lora_resolver_cache_dir (path traversal via lora name) functional claude-opus-5 https://github.com/vllm-project/vllm/issues/59270  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">vllm.plugins.lora_resolvers.filesystem_resolver.register_filesystem_resolver</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: FilesystemResolver loads adapters outside VLLM_LORA_RESOLVER_CACHE_DIR (path traversal via LoRA name)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/59270" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #59270 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm.models.deepseek_v4.common.mm_preprocess.deepseekv4vlimageprocessor [bug]: deepseek-v4 vl dummy image is not the worst case for multimodal profiling functional claude-opus-5 https://github.com/vllm-project/vllm/issues/59271  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm.models.deepseek_v4.common.mm_preprocess.DeepseekV4VLImageProcessor</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: DeepSeek-V4 VL dummy image is not the worst case for multimodal profiling</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/59271" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #59271 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm.v1.sample.thinking_budget_state.thinkingbudgetstateholder [bug]: thinkingbudgetstateholder maps every request to logits row 0 when spec decoding is on but a step has no drafts functional claude-opus-5 https://github.com/vllm-project/vllm/issues/59272  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm.v1.sample.thinking_budget_state.ThinkingBudgetStateHolder</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: ThinkingBudgetStateHolder maps every request to logits row 0 when spec decoding is on but a step has no drafts</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/59272" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #59272 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm.v1.sample.thinking_budget_state.thinkingbudgetstateholder [bug]: thinkingbudgetstateholder.sync_batch leaks stale state on unidirectional moves functional claude-opus-5 https://github.com/vllm-project/vllm/issues/59273  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm.v1.sample.thinking_budget_state.ThinkingBudgetStateHolder</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]: ThinkingBudgetStateHolder.sync_batch leaks stale state on unidirectional moves</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/59273" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #59273 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm_engine_reported/vllm-llm--engine-again;vllm_engine_reported/vllm-llm--engine-cutoff-window [bug]: vllm hangs indefinitely with low `num_gpu_blocks_override` crash claude-opus-4-8 https://github.com/vllm-project/vllm/issues/35541  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm_engine_reported/vllm-llm--engine-again;vllm_engine_reported/vllm-llm--engine-cutoff-window</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-4-8</span>
          </div>
          <div class="bug-title-text">[Bug]: vLLM hangs indefinitely with low `num_gpu_blocks_override`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/35541" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #35541 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vllm_engine_reported/vllm-llm--engine-again;vllm_engine_reported/vllm-llm--engine-cutoff-window [bug]: `block_size=8` triggers triton compilationerror in flexattention kernel; other backends correctly reject crash claude-opus-4-8 https://github.com/vllm-project/vllm/issues/39340  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vllm_engine_reported/vllm-llm--engine-again;vllm_engine_reported/vllm-llm--engine-cutoff-window</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-4-8</span>
          </div>
          <div class="bug-title-text">[Bug]: `block_size=8` triggers Triton CompilationError in FlexAttention kernel; other backends correctly reject</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/vllm-project/vllm/issues/39340" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #39340 ↗</a>
        </div>
      </div>
    </div>
  </div>
</details>
<details class="app-collapsible-card" id="app-sglang" data-app="sglang">
  <summary class="app-summary">
    <div class="app-summary-left">
      <svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="SGLang"><rect x="2" y="4" width="20" height="16" rx="4" fill="#F3E8FF"/><text x="12" y="15.5" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" font-weight="800" fill="#7C3AED" text-anchor="middle" letter-spacing="-0.02em">SGL</text></svg>
      <span class="app-name-text">SGLang</span>
      <span class="app-domain-pill">LLM Serving</span>
      <span class="app-count-badge">33 bugs</span>
    </div>
    <div class="app-summary-right">
      <div class="app-pills-row">
        <span class="mini-status-pill mini-confirmed">17 Confirmed</span>
        <span class="mini-status-pill mini-pending">15 Pending</span>
        <span class="mini-status-pill mini-rejected">1 Rejected</span>
      </div>
      <span class="app-chevron-icon" aria-hidden="true">▼</span>
    </div>
  </summary>
  <div class="app-details-body">
    <div class="bugs-cards-list">
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-parser-code-completion-parser fix(completion): treat none suffix as empty in fim prompt builder functional claude-opus-5 https://github.com/sgl-project/sglang/pull/31022  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-parser-code-completion-parser</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">fix(completion): treat None suffix as empty in FIM prompt builder</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/31022" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #31022 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-function-call-qwen25-detector [fix] keep normal text preceding the tool-call opener in streaming parsers functional claude-opus-5 https://github.com/sgl-project/sglang/pull/35169  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-function-call-qwen25-detector</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Fix] Keep normal text preceding the tool-call opener in streaming parsers</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/35169" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #35169 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-function-call-qwen25-detector;sglang-srt-function-call-function-call-parser-functioncallpa;sglang-srt-function-call-llama32-detector;sglang-srt-function-call-gigachat3-detector;sglang-srt-function-call-hermes-detector--long;sglang-srt-function-call-llama32-detector--long;sglang-srt-function-call-mistral-detector--long [bug] 9 tool-call parsers drop arguments when one streaming increment has more than one complete call functional claude-opus-5 https://github.com/sgl-project/sglang/issues/37634  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-function-call-qwen25-detector;sglang-srt-function-call-function-call-parser-functioncallpa;sglang-srt-function-call-llama32-detector;sglang-srt-function-call-gigachat3-detector;sglang-srt-function-call-hermes-detector--long;sglang-srt-function-call-llama32-detector--long;sglang-srt-function-call-mistral-detector--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] 9 tool-call parsers drop arguments when one streaming increment has more than one complete call</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/37634" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #37634 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-function-call-glm4-moe-detector;sglang-srt-function-call-glm4-moe-detector--long [bug]  8 tool-call parsers give wrong or missing calls in token-by-token streaming functional claude-opus-5 https://github.com/sgl-project/sglang/issues/35564  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-function-call-glm4-moe-detector;sglang-srt-function-call-glm4-moe-detector--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]  8 tool-call parsers give wrong or missing calls in token-by-token streaming</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/35564" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #35564 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-function-call-llama32-detector;sglang-srt-function-call-lfm2-detector--long;sglang-srt-function-call-llama32-detector--long fix(function_call): skip non-object entries in parse_base_json crash claude-opus-5 https://github.com/sgl-project/sglang/pull/37291  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-function-call-llama32-detector;sglang-srt-function-call-lfm2-detector--long;sglang-srt-function-call-llama32-detector--long</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">fix(function_call): skip non-object entries in parse_base_json</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/37291" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #37291 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-function-call-mimo-detector;sglang-srt-function-call-mimo-detector--long [bug] mimo tool-call streaming: text after the last tool call is silently dropped; split bot-token flushes markup into content functional claude-opus-5 https://github.com/sgl-project/sglang/issues/33186  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-function-call-mimo-detector;sglang-srt-function-call-mimo-detector--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] MiMo tool-call streaming: text after the last tool call is silently dropped; split bot-token flushes markup into content</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/33186" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #33186 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-function-call-trinity-detector fix(function_call): strip think tags split across stream chunks in trinity functional claude-opus-5 https://github.com/sgl-project/sglang/pull/30990  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-function-call-trinity-detector</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">fix(function_call): strip think tags split across stream chunks in Trinity</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/30990" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #30990 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-parser-reasoning-parser-reasoningparser;sglang-srt-parser-reasoning-parser-reasoningparser--long [fix] cohere command4: strip echoed `&lt;|start_thinking|&gt;` in streaming and flush the final text block functional claude-opus-5 https://github.com/sgl-project/sglang/pull/33225  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-parser-reasoning-parser-reasoningparser;sglang-srt-parser-reasoning-parser-reasoningparser--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Fix] Cohere Command4: strip echoed `&lt;|START_THINKING|&gt;` in streaming and flush the final text block</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/33225" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #33225 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-function-call-mimo-detector;sglang-srt-function-call-qwen3-coder-detector;sglang-srt-function-call-mimo-detector--long;sglang-srt-function-call-poolside-v1-detector--long fix(function_call): handle non-finite numbers in tool-call argument coercion crash claude-opus-5 https://github.com/sgl-project/sglang/pull/28797  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-function-call-mimo-detector;sglang-srt-function-call-qwen3-coder-detector;sglang-srt-function-call-mimo-detector--long;sglang-srt-function-call-poolside-v1-detector--long</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">fix(function_call): handle non-finite numbers in tool-call argument coercion</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/28797" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #28797 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="sglang-srt-layers-deep-gemm-wrapper-configurer [bug] jit deepgemm is enabled on sm121 (gb10 / dgx spark): the sm120 exclusion checks `== 120` instead of the consumer-blackwell family functional claude-opus-5 https://github.com/sgl-project/sglang/issues/36551  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">sglang-srt-layers-deep-gemm-wrapper-configurer</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] JIT DeepGEMM is enabled on SM121 (GB10 / DGX Spark): the SM120 exclusion checks `== 120` instead of the consumer-Blackwell family</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/36551" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #36551 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-parser-harmony-parser;sglang-srt-parser-harmony-parser--long [parser] hold back harmony markers split across streaming chunks functional claude-opus-5 https://github.com/sgl-project/sglang/pull/41017  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-parser-harmony-parser;sglang-srt-parser-harmony-parser--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[parser] Hold back harmony markers split across streaming chunks</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/41017" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #41017 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-constrained-xgrammar-backend--again;sglang-srt-constrained-xgrammar-backend--long fix: truncate xgrammar accepted_tokens in place on rollback functional claude-opus-5 https://github.com/sgl-project/sglang/pull/31728  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-constrained-xgrammar-backend--again;sglang-srt-constrained-xgrammar-backend--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">fix: truncate xgrammar accepted_tokens in place on rollback</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/31728" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #31728 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang.srt.function_call.apertus2509_detector.apertus2509detector apertus2509detector (streaming) drops the second tool block and trailing text when they arrive in the same chunk` functional claude-opus-5 https://github.com/sgl-project/sglang/issues/41821  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang.srt.function_call.apertus2509_detector.Apertus2509Detector</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">Apertus2509Detector (streaming) drops the second tool block and trailing text when they arrive in the same chunk`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/41821" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #41821 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-entrypoints-ollama-serving--long [ollama] map options.seed to the sampling_seed field crash claude-opus-5 https://github.com/sgl-project/sglang/pull/39131  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-entrypoints-ollama-serving--long</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Ollama] Map options.seed to the sampling_seed field</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/39131" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #39131 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-function-call-deepseekv3-detector--long tool-call parsers lose or corrupt data at streaming chunk boundaries (multiple detectors) functional claude-opus-5 https://github.com/sgl-project/sglang/issues/31915  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-function-call-deepseekv3-detector--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">Tool-call parsers lose or corrupt data at streaming chunk boundaries (multiple detectors)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/31915" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #31915 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-function-call-hunyuan-detector--long [fix] parse hunyuan tool arguments with json schema type arrays crash claude-opus-5 https://github.com/sgl-project/sglang/pull/38940  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-function-call-hunyuan-detector--long</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Fix] Parse Hunyuan tool arguments with JSON Schema type arrays</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/38940" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #38940 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-function-call-llama32-detector--long;sglang#1 [bugfix] flush pending tool calls at end of stream in the llama 3.2 detector functional claude-opus-5 https://github.com/sgl-project/sglang/pull/40994  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-function-call-llama32-detector--long;sglang#1</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Flush pending tool calls at end of stream in the Llama 3.2 detector</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/40994" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #40994 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-function-call-llama32-detector--long [bugfix] preserve single quotes inside json values in llama32 streaming tool calls functional claude-opus-5 https://github.com/sgl-project/sglang/pull/29582  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-function-call-llama32-detector--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bugfix] Preserve single quotes inside JSON values in Llama32 streaming tool calls</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/pull/29582" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">PR #29582 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang-srt-function-call-mistral-detector--long;sglang_1 tool-call parsers lose or corrupt data at streaming chunk boundaries (multiple detectors) functional claude-opus-5 https://github.com/sgl-project/sglang/issues/31915  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang-srt-function-call-mistral-detector--long;sglang_1</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">Tool-call parsers lose or corrupt data at streaming chunk boundaries (multiple detectors)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/31915" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #31915 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="sglang_0517/sglang-srt-function-call-deepseekv32-detector--0517;sglang_0517/sglang-srt-function-call-deepseekv4-detector--0517 [bug] deepseekv32/deepseekv4 tool-call parsers drop calls when the streamed output has two chunks crash claude-opus-5 https://github.com/sgl-project/sglang/issues/35563  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">sglang_0517/sglang-srt-function-call-deepseekv32-detector--0517;sglang_0517/sglang-srt-function-call-deepseekv4-detector--0517</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] deepseekv32/deepseekv4 tool-call parsers drop calls when the streamed output has two chunks</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/35563" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #35563 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-function-call-function-call-parser-functioncallpa [bug] deepseekv31detector.structure_info() omits `&lt;｜tool▁calls▁begin｜&gt;`, so its own detect_and_parse returns no tool call functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42131  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-function-call-function-call-parser-functioncallpa</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] DeepSeekV31Detector.structure_info() omits `&lt;｜tool▁calls▁begin｜&gt;`, so its own detect_and_parse returns no tool call</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42131" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42131 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-function-call-glm4-moe-detector;sglang-srt-function-call-glm4-moe-detector--long [bug] glm4moedetector streaming emits invalid json when a non-string parameter&#x27;s value is not valid json functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42132  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-function-call-glm4-moe-detector;sglang-srt-function-call-glm4-moe-detector--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] Glm4MoeDetector streaming emits invalid JSON when a non-string parameter&#x27;s value is not valid JSON</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42132" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42132 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-function-call-glm4-moe-detector;sglang-srt-function-call-glm4-moe-detector--long [bug]  glm4moedetector changes string-typed argument values that look like json (&quot;true&quot; → &quot;true&quot;, &quot;1.50&quot; → &quot;1.5&quot;) functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42133  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-function-call-glm4-moe-detector;sglang-srt-function-call-glm4-moe-detector--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug]  Glm4MoeDetector changes string-typed argument values that look like JSON (&quot;true&quot; → &quot;True&quot;, &quot;1.50&quot; → &quot;1.5&quot;)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42133" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42133 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-entrypoints-openai-protocol;sglang-srt-entrypoints-openai-protocol--long [bug] chatcompletionrequest.set_json_schema mutates the caller&#x27;s response_format schema (reused schemas change behaviour) functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42134  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-entrypoints-openai-protocol;sglang-srt-entrypoints-openai-protocol--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] ChatCompletionRequest.set_json_schema mutates the caller&#x27;s response_format schema (reused schemas change behaviour)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42134" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42134 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-function-call-cohere-command4-detector;sglang-srt-function-call-cohere-command4-detector--long [bug] cohere_command4 detector (streaming) drops the tool call when text and the whole action block arrive in one chunk functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42135  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-function-call-cohere-command4-detector;sglang-srt-function-call-cohere-command4-detector--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] cohere_command4 detector (streaming) drops the tool call when text and the whole action block arrive in one chunk</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42135" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42135 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-function-call-deepseekv31-detector;sglang-srt-function-call-deepseekv31-detector--long [bug] deepseekv31 detector (streaming) drops the text that shares a delta with the start of a tool call functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42136  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-function-call-deepseekv31-detector;sglang-srt-function-call-deepseekv31-detector--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] deepseekv31 detector (streaming) drops the text that shares a delta with the start of a tool call</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42136" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42136 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-function-call-deepseekv31-detector;sglang-srt-function-call-deepseekv31-detector--long [bug] deepseekv31 detector (streaming): greedy name regex drops a call and attaches the next call&#x27;s arguments to it functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42137  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-function-call-deepseekv31-detector;sglang-srt-function-call-deepseekv31-detector--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] deepseekv31 detector (streaming): greedy name regex drops a call and attaches the next call&#x27;s arguments to it</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42137" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42137 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-function-call-hunyuan-detector;sglang-srt-function-call-hunyuan-detector--long [bug] hunyuan detector (streaming): control characters in string arguments produce invalid, corrupted json functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42139  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-function-call-hunyuan-detector;sglang-srt-function-call-hunyuan-detector--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] hunyuan detector (streaming): control characters in string arguments produce invalid, corrupted JSON</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42139" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42139 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-function-call-trinity-detector [bug] trinity detector removes `&lt;think&gt;` / `&lt;/think&gt;` from inside tool-call arguments functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42140  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-function-call-trinity-detector</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] trinity detector removes `&lt;think&gt;` / `&lt;/think&gt;` from inside tool-call arguments</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42140" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42140 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-entrypoints-ollama-serving [bug] ollama streaming endpoints mangle the output when `--incremental-streaming-output` is on functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42141  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-entrypoints-ollama-serving</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] Ollama streaming endpoints mangle the output when `--incremental-streaming-output` is on</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42141" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42141 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-utils-hf-transformers-common [bug] `get_hf_text_config` raises attributeerror when `thinker_config` holds a dict `text_config` crash claude-opus-5 https://github.com/sgl-project/sglang/issues/42142  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-utils-hf-transformers-common</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] `get_hf_text_config` raises AttributeError when `thinker_config` holds a dict `text_config`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42142" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42142 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-parser-harmony-parser [bug] harmonyparser streaming: arguments of a tool call on the analysis channel are emitted as reasoning functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42143  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-parser-harmony-parser</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] HarmonyParser streaming: arguments of a tool call on the analysis channel are emitted as reasoning</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42143" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42143 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="sglang-srt-constrained-xgrammar-backend--again;sglang-srt-constrained-xgrammar-backend--long [bug] xgrammargrammarbackend._sanitize_structural_format` skips `optional`, `star`, `plus`, `repeat`, `dispatch`, `token_dispatch` and `token_triggered_tags`, so a `null` `json_schema` inside them is rejected functional claude-opus-5 https://github.com/sgl-project/sglang/issues/42144  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">sglang-srt-constrained-xgrammar-backend--again;sglang-srt-constrained-xgrammar-backend--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Bug] XGrammarGrammarBackend._sanitize_structural_format` skips `optional`, `star`, `plus`, `repeat`, `dispatch`, `token_dispatch` and `token_triggered_tags`, so a `null` `json_schema` inside them is rejected</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/sgl-project/sglang/issues/42144" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #42144 ↗</a>
        </div>
      </div>
    </div>
  </div>
</details>
<details class="app-collapsible-card" id="app-arangodb" data-app="arangodb">
  <summary class="app-summary">
    <div class="app-summary-left">
      <svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="ArangoDB"><path d="M12 2C8 2 4 8 4 14C4 18.5 7.5 22 12 22C16.5 22 20 18.5 20 14C20 8 16 2 12 2Z" fill="#2B8236"/><circle cx="12" cy="15" r="4.2" fill="#84CC16"/><circle cx="12" cy="15" r="2.5" fill="#65A30D"/></svg>
      <span class="app-name-text">ArangoDB</span>
      <span class="app-domain-pill">Graph Database</span>
      <span class="app-count-badge">24 bugs</span>
    </div>
    <div class="app-summary-right">
      <div class="app-pills-row">
        <span class="mini-status-pill mini-confirmed">6 Confirmed</span>
        <span class="mini-status-pill mini-pending">18 Pending</span>
      </div>
      <span class="app-chevron-icon" aria-hidden="true">▼</span>
    </div>
  </summary>
  <div class="app-details-body">
    <div class="bugs-cards-list">
      <div class="bug-card-row" data-status="Confirmed" data-search="aql-functions-string-substitute; co-author&#x27;s agentic-pbt run aql `substitute()` returns `null` for an empty input string functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23293  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">aql-functions-string-substitute; co-author&#x27;s Agentic-PBT run</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">AQL `SUBSTITUTE()` returns `null` for an empty input string</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23293" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23293 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="aql-functions-string-substitute; co-author&#x27;s agentic-pbt run `substitute` returns null and an icu warning for an empty input string functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23357  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">aql-functions-string-substitute; co-author&#x27;s Agentic-PBT run</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`SUBSTITUTE` returns null and an ICU warning for an empty input string</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23357" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23357 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="co-author&#x27;s agentic-pbt run `to_number` converts a valid subnormal decimal string to zero functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23358  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">co-author&#x27;s Agentic-PBT run</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`TO_NUMBER` converts a valid subnormal decimal string to zero</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23358" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23358 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="co-author&#x27;s agentic-pbt run append(null, [])` returns null instead of the other input array functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23359  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">co-author&#x27;s Agentic-PBT run</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">APPEND(null, [])` returns null instead of the other input array</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23359" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23359 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="co-author&#x27;s agentic-pbt run reverse corrupts a single astral unicode character functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23360  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">co-author&#x27;s Agentic-PBT run</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">REVERSE corrupts a single astral Unicode character</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23360" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23360 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="co-author&#x27;s agentic-pbt run `find_first` and `find_last` fail to find present control characters functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23361  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">co-author&#x27;s Agentic-PBT run</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`FIND_FIRST` and `FIND_LAST` fail to find present control characters</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23361" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23361 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="co-author&#x27;s agentic-pbt run `regex_matches` reports a match for an empty string that cannot match functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23362  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">co-author&#x27;s Agentic-PBT run</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`REGEX_MATCHES` reports a match for an empty string that cannot match</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23362" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23362 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="aql-operators-array-comparison-operators;aql-operators-array-comparison-operators--long at least (&lt;n&gt;) (&lt;expression&gt;) is true even when n is larger than the array&#x27;s length functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23363  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">aql-operators-array-comparison-operators;aql-operators-array-comparison-operators--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">AT LEAST (&lt;n&gt;) (&lt;expression&gt;) is true even when n is larger than the array&#x27;s length</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23363" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23363 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="aql-high-level-operations-limit--again;indexes-and-search-indexing-working-with-indexes-persistent--again persistent index with deterministic sort and offset limit incorrectly returns an empty result functional claude-opus-5 https://github.com/arangodb/arangodb/issues/22909  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">aql-high-level-operations-limit--again;indexes-and-search-indexing-working-with-indexes-persistent--again</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">Persistent index with deterministic SORT and offset LIMIT incorrectly returns an empty result</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/22909" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #22909 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="date_diff();date_iso8601() arangodb date_iso8601() applies the sign of a negative utc offset only to its hours, not its minutes functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23382  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">DATE_DIFF();DATE_ISO8601()</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">ArangoDB DATE_ISO8601() applies the sign of a negative UTC offset only to its hours, not its minutes</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23382" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23382 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="ngram_match() arangodb `ngram_match()` counts one attribute n-gram many times (stale dp diagonal) functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23383  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">NGRAM_MATCH()</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">ArangoDB `NGRAM_MATCH()` counts one attribute n-gram many times (stale DP diagonal)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23383" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23383 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="to_array() arangodb aql `sorted()` replaces distinct elements that compare equal functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23384  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">TO_ARRAY()</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">ArangoDB AQL `SORTED()` replaces distinct elements that compare equal</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23384" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23384 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="json_parse();pi() `json_parse` exponent numbers can read beyond the input string functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23385  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">JSON_PARSE();PI()</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`JSON_PARSE` exponent numbers can read beyond the input string</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23385" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23385 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="json_parse() `json_parse` can misround fractions and large integer tokens functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23386  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">JSON_PARSE()</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`JSON_PARSE` can misround fractions and large integer tokens</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23386" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23386 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="aql-execution-and-performance-query-optimization-optimizer-r aql `use-indexes` uses a sparse index for a range condition that can match `null` when an `or` branch proves non-null, dropping rows functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23396  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">aql-execution-and-performance-query-optimization-optimizer-r</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">AQL `use-indexes` uses a sparse index for a range condition that can match `null` when an `OR` branch proves non-null, dropping rows</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23396" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23396 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="aql-functions-string-substitute aql `substitute()` with several search values skips a match that starts right where the previous replacement ended functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23399  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">aql-functions-string-substitute</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">AQL `SUBSTITUTE()` with several search values skips a match that starts right where the previous replacement ended</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23399" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23399 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="aql-operators-arithmetic-operators aql arithmetic on 64-bit integers from documents loses precision; the same expression on literals does not functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23400  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">aql-operators-arithmetic-operators</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">AQL arithmetic on 64-bit integers from documents loses precision; the same expression on literals does not</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23400" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23400 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="aql-operators-ternary-operator aql `remove-redundant-calculations` treats `(a ? b : c) ? d : e` and `a ? b : (c ? d : e)` as the same calculation functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23397  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">aql-operators-ternary-operator</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">AQL `remove-redundant-calculations` treats `(a ? b : c) ? d : e` and `a ? b : (c ? d : e)` as the same calculation</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23397" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23397 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="develop-http-api-import `post /_api/import` stores duplicate attribute names from document and tabular input functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23401  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">develop-http-api-import</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`POST /_api/import` stores duplicate attribute names from document and tabular input</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23401" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23401 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="develop-http-api-import /_api/import` with `type=documents` and `complete=true` commits a partial import when a line is not valid json functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23398  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">develop-http-api-import</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">/_api/import` with `type=documents` and `complete=true` commits a partial import when a line is not valid JSON</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23398" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23398 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="indexes-and-search-indexing-working-with-indexes-persistent--again aql `collect` served from a persistent index merges the array values `[]` and `[null]` into one group functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23402  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">indexes-and-search-indexing-working-with-indexes-persistent--again</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">AQL `COLLECT` served from a persistent index merges the array values `[]` and `[null]` into one group</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23402" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23402 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="aql-operators-ternary-operator--again aql ternary operator evaluates an untaken operand when it contains an array expansion with a subquery crash claude-opus-5 https://github.com/arangodb/arangodb/issues/23403  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">aql-operators-ternary-operator--again</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">AQL ternary operator evaluates an untaken operand when it contains an array expansion with a subquery</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23403" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23403 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="arangodb#1;arangodb_1 `date_round` with a large positive amount terminates the server with sigfpe crash claude-opus-5 https://github.com/arangodb/arangodb/issues/23411  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">arangodb#1;arangodb_1</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`DATE_ROUND` with a large positive amount terminates the server with SIGFPE</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23411" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23411 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="arangodb#1;arangodb_1 `date_round` assigns pre-1970 timestamps to the following bucket functional claude-opus-5 https://github.com/arangodb/arangodb/issues/23412  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">arangodb#1;arangodb_1</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`DATE_ROUND` assigns pre-1970 timestamps to the following bucket</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/arangodb/arangodb/issues/23412" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #23412 ↗</a>
        </div>
      </div>
    </div>
  </div>
</details>
<details class="app-collapsible-card" id="app-cronie" data-app="cronie">
  <summary class="app-summary">
    <div class="app-summary-left">
      <svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="cronie"><circle cx="12" cy="12" r="9" stroke="#475569" stroke-width="2" fill="none"/><polyline points="12,7 12,12 15,14" stroke="#475569" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>
      <span class="app-name-text">cronie</span>
      <span class="app-domain-pill">System Daemon</span>
      <span class="app-count-badge">13 bugs</span>
    </div>
    <div class="app-summary-right">
      <div class="app-pills-row">
        <span class="mini-status-pill mini-confirmed">13 Confirmed</span>
      </div>
      <span class="app-chevron-icon" aria-hidden="true">▼</span>
    </div>
  </summary>
  <div class="app-details-body">
    <div class="bugs-cards-list">
      <div class="bug-card-row" data-status="Confirmed" data-search="crontab-1-description;crontab-1-t;crontab-5-extensions support input from a pipe for `crontab -t -` functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/223  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">crontab-1-description;crontab-1-t;crontab-5-extensions</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">Support input from a pipe for `crontab -T -`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/223" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #223 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="anacron-8-t `anacron -t` error stream contradicts its manual functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/224  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">anacron-8-t</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`anacron -T` error stream contradicts its manual</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/224" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #224 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="anacron-8-t;anacrontab-5-start-hours-range;anacrontab-5-description anacron: start_hours_range, random_delay and preferred_hour are matched by prefix, so other variables such as start_hours_range_old are rejected or silently change scheduling functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/226  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">anacron-8-t;anacrontab-5-start-hours-range;anacrontab-5-description</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">anacron: START_HOURS_RANGE, RANDOM_DELAY and PREFERRED_HOUR are matched by prefix, so other variables such as START_HOURS_RANGE_OLD are rejected or silently change scheduling</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/226" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #226 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="anacron-8-t;anacrontab-5-description anacron: misspelled period macros such as `@monthlyxyz` are accepted as `@monthly`, and a job with an unknown macro runs although anacron says it is skipped functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/227  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">anacron-8-t;anacrontab-5-description</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">anacron: misspelled period macros such as `@monthlyXYZ` are accepted as `@monthly`, and a job with an unknown macro runs although anacron says it is skipped</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/227" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #227 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="anacrontab-5-start-hours-range anacron: start_hours_range hours are not range-checked (and overflow `int`), so invalid ranges pass `anacron -t` and silently stop all jobs functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/231  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">anacrontab-5-start-hours-range</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">anacron: START_HOURS_RANGE hours are not range-checked (and overflow `int`), so invalid ranges pass `anacron -T` and silently stop all jobs</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/231" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #231 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="cronnext-1-t cronnext: `-t` and `-q` parse the epoch time with `atoi()`, so times from 2038-01-19 on are truncated (y2038) functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/228  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">cronnext-1-t</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">cronnext: `-t` and `-q` parse the epoch time with `atoi()`, so times from 2038-01-19 on are truncated (Y2038)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/228" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #228 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="crontab-5-extensions @daily`/`@midnight` and `@hourly` do not set `dom_star`/`dow_star`, unlike their documented equivalents (cf. #52) functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/229  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">crontab-5-extensions</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">@daily`/`@midnight` and `@hourly` do not set `DOM_STAR`/`DOW_STAR`, unlike their documented equivalents (cf. #52)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/229" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #229 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="crontab-5-description `cronnext` ignores a stepped day-of-week / day-of-month field functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/215  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">crontab-5-description</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`cronnext` ignores a stepped day-of-week / day-of-month field</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/215" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #215 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="crontab-5-description reversed ranges are accepted but never match functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/221  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">crontab-5-description</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">reversed ranges are accepted but never match</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/221" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #221 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="crontab-5-cron-tz `cronnext` ignores `cron_tz` functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/222  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">crontab-5-cron-tz</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`cronnext` ignores `CRON_TZ`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/222" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #222 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="cronnext-1 cronnext reports a time one hour late when skipping to a month with a different dst state functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/217  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">cronnext-1</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">cronnext reports a time one hour late when skipping to a month with a different DST state</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/217" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #217 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="cronnext-1 cronnext can skip an entire matching day across a dst spring-forward transition functional claude-opus-5 https://github.com/cronie-crond/cronie/issues/218  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">cronnext-1</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">cronnext can skip an entire matching day across a DST spring-forward transition</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/218" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #218 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="anacrontab-5-description anacron: a large `random_delay` value crashes anacron with sigfpe or makes it loop forever crash claude-opus-5 https://github.com/cronie-crond/cronie/issues/230  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">anacrontab-5-description</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">anacron: a large `RANDOM_DELAY` value crashes anacron with SIGFPE or makes it loop forever</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/cronie-crond/cronie/issues/230" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #230 ↗</a>
        </div>
      </div>
    </div>
  </div>
</details>
<details class="app-collapsible-card" id="app-postgresql" data-app="postgresql">
  <summary class="app-summary">
    <div class="app-summary-left">
      <svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="PostgreSQL"><path d="M12 3C8 3 4 5 4 10C4 13.5 5.5 17 8 19V22H11V18H13V22H16V19C18.5 17 20 13.5 20 10C20 5 16 3 12 3Z" fill="#336791"/><circle cx="9.5" cy="9.5" r="1.5" fill="#FFFFFF"/><circle cx="14.5" cy="9.5" r="1.5" fill="#FFFFFF"/><path d="M11 12H13V15H11V12Z" fill="#E2E8F0"/></svg>
      <span class="app-name-text">PostgreSQL</span>
      <span class="app-domain-pill">Database Engine</span>
      <span class="app-count-badge">10 bugs</span>
    </div>
    <div class="app-summary-right">
      <div class="app-pills-row">
        <span class="mini-status-pill mini-confirmed">2 Confirmed</span>
        <span class="mini-status-pill mini-pending">8 Pending</span>
      </div>
      <span class="app-chevron-icon" aria-hidden="true">▼</span>
    </div>
  </summary>
  <div class="app-details-body">
    <div class="bugs-cards-list">
      <div class="bug-card-row" data-status="Pending" data-search="pg_backup_start pg_backup_start accepts a newline in the label, and the backup will not start functional claude-opus-5 https://www.postgresql.org/account/submitbug/19730/  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">pg_backup_start</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">pg_backup_start accepts a newline in the label, and the backup will not start</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://www.postgresql.org/account/submitbug/19730/" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Tracker ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="last_value first_value/last_value/nth_value return null under exclude ties when the current row is outside its frame functional claude-opus-5 https://www.postgresql.org/account/submitbug/19731/  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">last_value</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">first_value/last_value/nth_value return NULL under EXCLUDE TIES when the current row is outside its frame</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://www.postgresql.org/account/submitbug/19731/" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Tracker ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="last_value first_value/last_value/nth_value return null under exclude ties when the current row is outside its frame functional claude-opus-5 https://www.postgresql.org/account/submitbug/19732/  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">last_value</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">first_value/last_value/nth_value return NULL under EXCLUDE TIES when the current row is outside its frame</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://www.postgresql.org/account/submitbug/19732/" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Tracker ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="json_object an empty json_object rejects the on null and with unique keys clauses that its documented syntax allows functional claude-opus-5 https://www.postgresql.org/account/submitbug/19737/  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">json_object</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">an empty JSON_OBJECT rejects the ON NULL and WITH UNIQUE KEYS clauses that its documented syntax allows</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://www.postgresql.org/account/submitbug/19737/" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Tracker ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="transaction_timestamp transaction_timestamp() and statement_timestamp() differ for a parameterized first statement, which the documentation says return the same value functional claude-opus-5 https://www.postgresql.org/account/submitbug/19739/  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">transaction_timestamp</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">transaction_timestamp() and statement_timestamp() differ for a parameterized first statement, which the documentation says return the same value</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://www.postgresql.org/account/submitbug/19739/" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Tracker ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="has_language_privilege has_language_privilege returns true for a nonexistent language oid when the current user is a superuser, where a named non-superuser gets null functional claude-opus-5 https://www.postgresql.org/account/submitbug/19740/  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">has_language_privilege</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">has_language_privilege returns true for a nonexistent language OID when the current user is a superuser, where a named non-superuser gets null</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://www.postgresql.org/account/submitbug/19740/" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Tracker ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="avg avg(double precision) overflows on cancelling finite inputs whose mean is representable functional claude-opus-5 https://www.postgresql.org/account/submitbug/19741/  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">avg</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">avg(double precision) overflows on cancelling finite inputs whose mean is representable</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://www.postgresql.org/account/submitbug/19741/" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Tracker ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="jsonb_object_agg_unique_strict (round 003-jsonb-object-agg-unique-strict) jsonb_object_agg_unique_strict silently discards a jsonb null value functional claude-opus-5 https://www.postgresql.org/account/submitbug/19735/  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">jsonb_object_agg_unique_strict (round 003-jsonb-object-agg-unique-strict)</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">jsonb_object_agg_unique_strict silently discards a JSONB null value</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://www.postgresql.org/account/submitbug/19735/" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Tracker ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="json_object (round 004-json-object) json_object with absent on null accepts a null key and an array, composite or json key for the omitted pair functional claude-opus-5 https://www.postgresql.org/account/submitbug/19736/  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">json_object (round 004-json-object)</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">JSON_OBJECT with ABSENT ON NULL accepts a NULL key and an array, composite or JSON key for the omitted pair</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://www.postgresql.org/account/submitbug/19736/" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Tracker ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="uuidv7 (round 009-uuidv7) uuidv7(interval) rejects timestamps 1 to 999 microseconds into the last millisecond its field can hold functional claude-opus-5 https://www.postgresql.org/account/submitbug/19738/  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">uuidv7 (round 009-uuidv7)</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">uuidv7(interval) rejects timestamps 1 to 999 microseconds into the last millisecond its field can hold</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://www.postgresql.org/account/submitbug/19738/" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Tracker ↗</a>
        </div>
      </div>
    </div>
  </div>
</details>
<details class="app-collapsible-card" id="app-clang_llvm" data-app="clang_llvm">
  <summary class="app-summary">
    <div class="app-summary-left">
      <svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Clang / LLVM"><path d="M4 18C4 18 7 19 10 16C13 13 13 8 13 8C13 8 15 11 17 12C19 13 21 12 21 12C21 12 19 15 16 17C13 19 8 20 4 18Z" fill="#D9381E"/><path d="M13 8C11 5 7 4 7 4C7 4 8 7 10 9C11 10 13 8 13 8Z" fill="#EA580C"/></svg>
      <span class="app-name-text">Clang / LLVM</span>
      <span class="app-domain-pill">Compiler / Toolchain</span>
      <span class="app-count-badge">9 bugs</span>
    </div>
    <div class="app-summary-right">
      <div class="app-pills-row">
        <span class="mini-status-pill mini-confirmed">6 Confirmed</span>
        <span class="mini-status-pill mini-pending">3 Pending</span>
      </div>
      <span class="app-chevron-icon" aria-hidden="true">▼</span>
    </div>
  </summary>
  <div class="app-details-body">
    <div class="bugs-cards-list">
      <div class="bug-card-row" data-status="Confirmed" data-search="alignment-builtins [clang] assertion `is&lt;typeinfolvalue&gt;() &amp;&amp; &quot;not a type_info lvalue&quot;&#x27; failed with alignment builtins crash claude-opus-5 https://github.com/llvm/llvm-project/issues/216999  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">alignment-builtins</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[Clang] Assertion `is&lt;TypeInfoLValue&gt;() &amp;&amp; &quot;not a type_info lvalue&quot;&#x27; failed with alignment builtins</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/llvm/llvm-project/issues/216999" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #216999 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="__is_bitwise_cloneable clang `__is_bitwise_cloneable` hangs the compiler on nested structs (exponential, un-memoized recursion) crash claude-opus-5 https://github.com/llvm/llvm-project/issues/227446  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">__is_bitwise_cloneable</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">clang `__is_bitwise_cloneable` hangs the compiler on nested structs (exponential, un-memoized recursion)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/llvm/llvm-project/issues/227446" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #227446 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="model attribute clang `model` attribute silently ignored when the variable was referenced before its definition functional claude-opus-5 https://github.com/llvm/llvm-project/issues/227447  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">model attribute</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">clang `model` attribute silently ignored when the variable was referenced before its definition</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/llvm/llvm-project/issues/227447" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #227447 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="vectorcall attribute clang misassigns homogeneous vector aggregate arguments for sysv `vectorcall` functional claude-opus-5 https://github.com/llvm/llvm-project/issues/227451  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">vectorcall attribute</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">Clang misassigns homogeneous vector aggregate arguments for SysV `vectorcall`</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/llvm/llvm-project/issues/227451" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #227451 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="vectorcall attribute clang `__attribute__((vectorcall))` crashes on any `long double` parameter (x86_64 linux) crash claude-opus-5 https://github.com/llvm/llvm-project/issues/227448  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">vectorcall attribute</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">clang `__attribute__((vectorcall))` crashes on any `long double` parameter (x86_64 Linux)</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/llvm/llvm-project/issues/227448" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #227448 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="alignment builtins [clang] `constexpr` `__builtin_align_down/up` on a pointer into an array reads the original element functional claude-opus-5 https://github.com/llvm/llvm-project/issues/227548  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">Alignment builtins</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">[clang] `constexpr` `__builtin_align_down/up` on a pointer into an array reads the original element</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/llvm/llvm-project/issues/227548" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #227548 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="builtin-convertvector `__builtin_convertvector` from `__bf16` to `long double` vectors gives wrong values crash claude-opus-5 https://github.com/llvm/llvm-project/issues/228648  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">builtin-convertvector</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`__builtin_convertvector` from `__bf16` to `long double` vectors gives wrong values</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/llvm/llvm-project/issues/228648" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #228648 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="builtin-convertvector `__builtin_convertvector` to a `bool` vector folds 0.5 to `false` in a constant expression functional claude-opus-5 https://github.com/llvm/llvm-project/issues/228649  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">builtin-convertvector</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`__builtin_convertvector` to a `bool` vector folds 0.5 to `false` in a constant expression</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/llvm/llvm-project/issues/228649" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #228649 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="nonnull attribute `nonnull` whose every index is rejected becomes &quot;all pointers&quot; and changes code functional claude-opus-5 https://github.com/llvm/llvm-project/issues/228670  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">nonnull attribute</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">`nonnull` whose every index is rejected becomes &quot;all pointers&quot; and changes code</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://github.com/llvm/llvm-project/issues/228670" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Issue #228670 ↗</a>
        </div>
      </div>
    </div>
  </div>
</details>
<details class="app-collapsible-card" id="app-gcc" data-app="gcc">
  <summary class="app-summary">
    <div class="app-summary-left">
      <svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="GCC"><rect x="2" y="4" width="20" height="16" rx="4" fill="#FEE2E2"/><text x="12" y="15.5" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" font-weight="800" fill="#991B1B" text-anchor="middle" letter-spacing="-0.02em">GCC</text></svg>
      <span class="app-name-text">GCC</span>
      <span class="app-domain-pill">Compiler / Toolchain</span>
      <span class="app-count-badge">5 bugs</span>
    </div>
    <div class="app-summary-right">
      <div class="app-pills-row">
        <span class="mini-status-pill mini-confirmed">3 Confirmed</span>
        <span class="mini-status-pill mini-pending">1 Pending</span>
        <span class="mini-status-pill mini-rejected">1 Rejected</span>
      </div>
      <span class="app-chevron-icon" aria-hidden="true">▼</span>
    </div>
  </summary>
  <div class="app-details-body">
    <div class="bugs-cards-list">
      <div class="bug-card-row" data-status="Confirmed" data-search="builtin-is-virtual-base-of __builtin_is_virtual_base_of reports a non-virtual base reached through a virtual base as virtual functional claude-opus-5 https://gcc.gnu.org/bugzilla/show_bug.cgi?id=127487  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">builtin-is-virtual-base-of</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">__builtin_is_virtual_base_of reports a non-virtual base reached through a virtual base as virtual</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://gcc.gnu.org/bugzilla/show_bug.cgi?id=127487" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">GCC #127487 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="builtin-stdc-rotate-left the manual&#x27;s equivalent expression for __builtin_stdc_rotate_left/right is wrong for non-power-of-two _bitint widths functional claude-opus-5 https://gcc.gnu.org/bugzilla/show_bug.cgi?id=127490  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">builtin-stdc-rotate-left</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">the manual&#x27;s equivalent expression for __builtin_stdc_rotate_left/right is wrong for non-power-of-two _BitInt widths</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://gcc.gnu.org/bugzilla/show_bug.cgi?id=127490" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">GCC #127490 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Rejected" data-search="hardbool-attribute implicitly zero-initialized hardbool objects hold zero bits instead of the false representation functional claude-opus-5 https://gcc.gnu.org/bugzilla/show_bug.cgi?id=127486  rejected">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-rejected"><span class="status-dot dot-rejected"></span>Rejected</span>
            <span class="bug-api-code">hardbool-attribute</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">implicitly zero-initialized hardbool objects hold zero bits instead of the false representation</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://gcc.gnu.org/bugzilla/show_bug.cgi?id=127486" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">GCC #127486 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="macros-with-a-variable-number-of-arguments the gcc manual says , ## __va_args__ drops the comma for an empty argument; the cpp manual and gcc keep it functional claude-opus-5 https://gcc.gnu.org/bugzilla/show_bug.cgi?id=127491  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">macros-with-a-variable-number-of-arguments</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">the GCC manual says , ## __VA_ARGS__ drops the comma for an empty argument; the CPP manual and GCC keep it</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://gcc.gnu.org/bugzilla/show_bug.cgi?id=127491" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">GCC #127491 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="__builtin_bitreverseg __builtin_bitreverseg on a dependent c++ operand gives an ice in mangle_decl crash claude-opus-5 https://gcc.gnu.org/bugzilla/show_bug.cgi?id=127668  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">__builtin_bitreverseg</span>
            <span class="bug-type-pill">Crash</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">__builtin_bitreverseg on a dependent C++ operand gives an ICE in mangle_decl</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://gcc.gnu.org/bugzilla/show_bug.cgi?id=127668" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">GCC #127668 ↗</a>
        </div>
      </div>
    </div>
  </div>
</details>
<details class="app-collapsible-card" id="app-openssh" data-app="openssh">
  <summary class="app-summary">
    <div class="app-summary-left">
      <svg class="app-logo-svg" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="OpenSSH"><path d="M12 2L4 6V12C4 17 7.5 21 12 22C16.5 21 20 17 20 12V6L12 2Z" fill="#0F766E"/><circle cx="12" cy="10" r="2.5" fill="#CCFBF1"/><path d="M11 12.5H13V16H11V12.5Z" fill="#CCFBF1"/></svg>
      <span class="app-name-text">OpenSSH</span>
      <span class="app-domain-pill">Security / Network</span>
      <span class="app-count-badge">5 bugs</span>
    </div>
    <div class="app-summary-right">
      <div class="app-pills-row">
        <span class="mini-status-pill mini-confirmed">1 Confirmed</span>
        <span class="mini-status-pill mini-pending">4 Pending</span>
      </div>
      <span class="app-chevron-icon" aria-hidden="true">▼</span>
    </div>
  </summary>
  <div class="app-details-body">
    <div class="bugs-cards-list">
      <div class="bug-card-row" data-status="Pending" data-search="ssh-1-g ssh -g prints escapechar ^a as \^a which does not parse back functional claude-opus-5 https://bugzilla.mindrot.org/show_bug.cgi?id=4008  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">ssh-1-g</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">ssh -G prints EscapeChar ^A as \^A which does not parse back</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://bugzilla.mindrot.org/show_bug.cgi?id=4008" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Bugzilla #4008 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="ssh-1-g ssh -g shows some localforward entries as dynamicforward functional claude-opus-5 https://bugzilla.mindrot.org/show_bug.cgi?id=4009  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">ssh-1-g</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">ssh -G shows some LocalForward entries as DynamicForward</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://bugzilla.mindrot.org/show_bug.cgi?id=4009" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Bugzilla #4009 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="ssh-keygen-1-s ssh-keygen -s signs certificates with duplicate options, which sshd rejects functional claude-opus-5 https://bugzilla.mindrot.org/show_bug.cgi?id=4010  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">ssh-keygen-1-s</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">ssh-keygen -s signs certificates with duplicate options, which sshd rejects</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://bugzilla.mindrot.org/show_bug.cgi?id=4010" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Bugzilla #4010 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Confirmed" data-search="ssh-1-g--long streamlocalbindmask ignores host and match blocks, and the last value wins functional claude-opus-5 https://bugzilla.mindrot.org/show_bug.cgi?id=4013  confirmed">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-confirmed"><span class="status-dot dot-confirmed"></span>Confirmed</span>
            <span class="bug-api-code">ssh-1-g--long</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">StreamLocalBindMask ignores Host and Match blocks, and the last value wins</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://bugzilla.mindrot.org/show_bug.cgi?id=4013" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Bugzilla #4013 ↗</a>
        </div>
      </div>
      <div class="bug-card-row" data-status="Pending" data-search="openssh#1;openssh_1 ssh-keygen -f and -r miss a hashed known_hosts entry when the host name&#x27;s case differs functional claude-opus-5 https://bugzilla.mindrot.org/show_bug.cgi?id=4014  pending">
        <div class="bug-row-main">
          <div class="bug-row-tags">
            <span class="bug-status-badge badge-pending"><span class="status-dot dot-pending"></span>Pending</span>
            <span class="bug-api-code">openssh#1;openssh_1</span>
            <span class="bug-type-pill">Functional</span>
            <span class="bug-tool-pill">claude-opus-5</span>
          </div>
          <div class="bug-title-text">ssh-keygen -F and -R miss a hashed known_hosts entry when the host name&#x27;s case differs</div>
        </div>
        <div class="bug-row-actions">
          <a href="https://bugzilla.mindrot.org/show_bug.cgi?id=4014" target="_blank" rel="noopener noreferrer" class="bug-link-btn" title="View bug tracker entry">Bugzilla #4014 ↗</a>
        </div>
      </div>
    </div>
  </div>
</details>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script>
(function() {
  // 1. Chart.js Donut Initialization
  function initChart() {
    const ctx = document.getElementById('statusDonutChart');
    if (!ctx || typeof Chart === 'undefined') return;

    new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: ['Confirmed', 'Fixed', 'Pending', 'Rejected'],
        datasets: [{
          data: [177, 37, 79, 30],
          backgroundColor: ['#10b981', '#3b82f6', '#f59e0b', '#ef4444'],
          borderWidth: 2,
          borderColor: '#ffffff',
          hoverOffset: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '72%',
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: function(context) {
                const val = context.parsed;
                const total = 323;
                const pct = ((val / total) * 100).toFixed(1);
                return ' ' + context.label + ': ' + val + ' (' + pct + '%)';
              }
            }
          }
        }
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChart);
  } else {
    initChart();
  }

  // 2. Global helper to toggle an accordion and scroll to it
  window.toggleAppAccordion = function(slug) {
    const el = document.getElementById('app-' + slug);
    if (!el) return;
    el.open = true;
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  // 3. Search and Status Filtering
  document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('bugSearchInput');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const expandAllBtn = document.getElementById('expandAllBtn');
    const collapseAllBtn = document.getElementById('collapseAllBtn');
    const visibleCountEl = document.getElementById('visibleCount');
    const noBugsMsg = document.getElementById('noBugsMessage');
    const appCards = document.querySelectorAll('.app-collapsible-card');

    let activeFilter = 'all';

    function applyFilters() {
      const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
      let visibleCount = 0;

      appCards.forEach(function(card) {
        let cardHasMatch = false;
        const rows = card.querySelectorAll('.bug-card-row');

        rows.forEach(function(row) {
          const rowStatus = row.getAttribute('data-status');
          const rowSearch = row.getAttribute('data-search') || '';

          const statusMatch = (activeFilter === 'all') || (rowStatus === activeFilter);
          const queryMatch = !query || rowSearch.indexOf(query) !== -1;

          if (statusMatch && queryMatch) {
            row.style.display = '';
            visibleCount++;
            cardHasMatch = true;
          } else {
            row.style.display = 'none';
          }
        });

        if (cardHasMatch) {
          card.style.display = '';
          if (query || activeFilter !== 'all') {
            card.open = true;
          }
        } else {
          card.style.display = 'none';
        }
      });

      if (visibleCountEl) {
        visibleCountEl.textContent = visibleCount;
      }
      if (noBugsMsg) {
        noBugsMsg.style.display = (visibleCount === 0) ? 'block' : 'none';
      }
    }

    if (searchInput) {
      searchInput.addEventListener('input', applyFilters);
    }

    filterBtns.forEach(function(btn) {
      btn.addEventListener('click', function() {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilter = btn.getAttribute('data-filter') || 'all';
        applyFilters();
      });
    });

    if (expandAllBtn) {
      expandAllBtn.addEventListener('click', function() {
        appCards.forEach(card => card.open = true);
      });
    }

    if (collapseAllBtn) {
      collapseAllBtn.addEventListener('click', function() {
        appCards.forEach(card => card.open = false);
      });
    }
  });
})();
</script>

</div>
