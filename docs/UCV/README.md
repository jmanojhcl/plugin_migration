<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>HCL DevOps Velocity Plugins</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }

    h1 {
      text-align: left;
      color: #333;
    }

    .filter-buttons {
      text-align: left;
      margin-bottom: 20px;
    }

    .filter-buttons button {
      margin: 5px;
      padding: 10px 15px;
      border: none;
      background-color: #007bff;
      color: white;
      border-radius: 4px;
      cursor: pointer;
    }

    .filter-buttons button:hover {
      background-color: #0056b3;
    }

    .plugin-container {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: flex-start; 
    }

    .plugin-card {
      background-color: white;
      border-radius: 8px;
      padding: 20px;
      width: 250px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      transition: transform 0.2s;
    }

    .plugin-card:hover {
      transform: scale(1.03);
    }

    .plugin-title {
      font-size: 18px;
      font-weight: bold;
      margin-bottom: 10px;
      color: #333;
    }

    .plugin-category {
      font-size: 14px;
      color: #555;
    }

    .hidden {
      display: none;
    }
  </style>
</head>
<body>

  <h1>HCL DevOps Velocity Plugins - All plugins</h1>

  <h2>Filter by category:</h2>

  <div class="filter-buttons">
    <button onclick="filterPlugins('all')">All</button>
    <button onclick="filterPlugins('Artifact Management')">Artifact Management</button>
    <button onclick="filterPlugins('Automated Testing')">Automated Testing</button>
    <button onclick="filterPlugins('Automation')">Automation</button>
    <button onclick="filterPlugins('Business Value')">Business Value</button>
    <button onclick="filterPlugins('Continuous Deployment')">Continuous Deployment</button>
    <button onclick="filterPlugins('Continuous Integration')">Continuous Integration</button>
    <button onclick="filterPlugins('Data Virtualization')">Data Virtualization</button>
    <button onclick="filterPlugins('Database')">Database</button>
    <button onclick="filterPlugins('File Management')">File Management</button>
    <button onclick="filterPlugins('Issue Tracking')">Issue Tracking</button>
    <button onclick="filterPlugins('Mainframe')">Mainframe</button>
    <button onclick="filterPlugins('Middleware')">Middleware</button>
    <button onclick="filterPlugins('Security Scan')">Security Scan</button>
    <button onclick="filterPlugins('Source Control')">Source Control</button>
    <button onclick="filterPlugins('Test Data Management')">Test Data Management</button>
  </div>

  <div class="plugin-container">
    <div class="plugin-card" data-category="Automation">
        <div class="plugin-title">
            <a href="ucv-ext-aha/index.html" target="_blank">Aha!</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automated Testing">
        <div class="plugin-title">
            <a href="ucv-ext-jmeter/index.html" target="_blank">Apache JMeter</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Security Scan">
        <div class="plugin-title">
            <a href="ucv-ext-azure/index.html" target="_blank">Azure DevOps</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Source Control">
        <div class="plugin-title">
            <a href="ucv-ext-bitbucket-cloud/index.html" target="_blank">BitBucket Cloud</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Source Control">
        <div class="plugin-title">
            <a href="ucv-ext-bitbucket-server/index.html" target="_blank">BitBucket Server</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Security Scan">
        <div class="plugin-title">
            <a href="ucv-ext-blackduck/index.html" target="_blank">Black Duck</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Business Value">
        <div class="plugin-title">
            <a href="ucv-ext-bottleneck-detection/index.html" target="_blank">Bottleneck Detection</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Continuous Integration">
        <div class="plugin-title">
            <a href="ucv-ext-circleci/index.html" target="_blank">CircleCI</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Business Value">
        <div class="plugin-title">
            <a href="ucv-ext-coverage-core/index.html" target="_blank">Code Coverage</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Issue Tracking">
        <div class="plugin-title">
            <a href="ucv-ext-versionone/index.html" target="_blank">CollabNet VersionOne</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automated Testing">
        <div class="plugin-title">
            <a href="ucv-ext-cucumber/index.html" target="_blank">Cucumber</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automated Testing">
        <div class="plugin-title">
            <a href="ucv-ext-cypress/index.html" target="_blank">Cypress</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Continuous Integration">
        <div class="plugin-title">
            <a href="ucv-ext-build/index.html" target="_blank">DevOps Build</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Source Control">
        <div class="plugin-title">
            <a href="ucv-ext-control/index.html" target="_blank">DevOps Control</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Continuous Deployment">
        <div class="plugin-title">
            <a href="ucv-ext-ucd/index.html" target="_blank">DevOps Deploy</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Issue Tracking">
        <div class="plugin-title">
            <a href="ucv-ext-plan/index.html" target="_blank">DevOps Plan</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automated Testing">
        <div class="plugin-title">
            <a href="ucv-ext-onetest/index.html" target="_blank">DevOps Test</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automated Testing">
        <div class="plugin-title">
            <a href="ucv-ext-onetest-server/index.html" target="_blank">DevOps Test Hub</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Business Value">
        <div class="plugin-title">
            <a href="ucv-ext-agility/index.html" target="_blank">Digital.ai Agility</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Security Scan">
        <div class="plugin-title">
            <a href="ucv-ext-fortify-ssc/index.html" target="_blank">Fortify SSC</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Business Value">
        <div class="plugin-title">
            <a href="ucv-ext-release-summary-ibm/index.html" target="_blank">GenAI summary release IBM</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Business Value">
        <div class="plugin-title">
            <a href="ucv-ext-release-summary-openai/index.html" target="_blank">GenAI summary release OpenAI</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Source Control">
        <div class="plugin-title">
            <a href="ucv-ext-github/index.html" target="_blank">GitHub</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Source Control">
        <div class="plugin-title">
            <a href="ucv-ext-dependabot/index.html" target="_blank">GitHub Dependabot</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Source Control">
        <div class="plugin-title">
            <a href="ucv-ext-gitlab/index.html" target="_blank">GitLab</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Security Scan">
        <div class="plugin-title">
            <a href="ucv-ext-appscan/index.html" target="_blank">HCL AppScan Enterprise (ASE)</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Security Scan">
        <div class="plugin-title">
            <a href="ucv-ext-asoc/index.html" target="_blank">HCL AppScan on Cloud (ASoC)</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Business Value">
        <div class="plugin-title">
            <a href="ucv-ext-handlebars-reporter/index.html" target="_blank">Handlebar Reporter</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automated Testing">
        <div class="plugin-title">
            <a href="ucv-ext-rtas/index.html" target="_blank">IBM DevOps Test Hub</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Issue Tracking">
        <div class="plugin-title">
            <a href="ucv-ext-ewm/index.html" target="_blank">IBM Engineering Workflow Management (EWM)</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Continuous Integration">
        <div class="plugin-title">
            <a href="ucv-ext-jenkins/index.html" target="_blank">Jenkins</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Continuous Integration">
        <div class="plugin-title">
            <a href="urbancode-velocity/index.html" target="_blank">Jenkins (legacy)</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automated Testing">
        <div class="plugin-title">
            <a href="ucv-ext-junit/index.html" target="_blank">JUnit</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Issue Tracking">
        <div class="plugin-title">
            <a href="ucv-ext-jira/index.html" target="_blank">Jira</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Issue Tracking">
        <div class="plugin-title">
            <a href="ucv-ext-jira-service-management/index.html" target="_blank">Jira Service Management</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automated Testing">
        <div class="plugin-title">
            <a href="ucv-ext-vs-quality/index.html" target="_blank">Microsoft Visual Studio Testing</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Business Value">
        <div class="plugin-title">
            <a href="ucv-ext-milestone-risk-estimator/index.html" target="_blank">Milestone Risk Estimator</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automated Testing">
        <div class="plugin-title">
            <a href="ucv-ext-njs-unit/index.html" target="_blank">Njs-Unit</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Issue Tracking">
        <div class="plugin-title">
            <a href="ucv-ext-leankit/index.html" target="_blank">Planview Leankit</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Issue Tracking">
        <div class="plugin-title">
            <a href="ucv-ext-rally/index.html" target="_blank">Rally</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Issue Tracking">
        <div class="plugin-title">
            <a href="ucv-ext-sap-charm/index.html" target="_blank">SAP ChaRM</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automated Testing">
        <div class="plugin-title">
            <a href="selenium-ucv/index.html" target="_blank">Selenium</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Issue Tracking">
        <div class="plugin-title">
            <a href="ucv-ext-servicenow/index.html" target="_blank">ServiceNow</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automation">
        <div class="plugin-title">
            <a href="ucv-ext-shell/index.html" target="_blank">Shell</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Security Scan">
        <div class="plugin-title">
            <a href="ucv-ext-snyk/index.html" target="_blank">Snyk</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Security Scan">
        <div class="plugin-title">
            <a href="ucv-ext-sonar/index.html" target="_blank">SonarQube</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Business Value">
        <div class="plugin-title">
            <a href="ucv-ext-summary/index.html" target="_blank">Summary</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Security Scan">
        <div class="plugin-title">
            <a href="ucv-ext-tenable/index.html" target="_blank">Tenable.io</a>
        </div>
    </div>
    <div class="plugin-card" data-category="Automated Testing">
        <div class="plugin-title">
            <a href="ucv-ext-xray/index.html" target="_blank">Xray</a>
        </div>
    </div>

  </div>

  <script>
    function filterPlugins(category) {
      const cards = document.querySelectorAll('.plugin-card');
      cards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');
        if (category === 'all' || cardCategory === category) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    }
  </script>

</body>
</html>
