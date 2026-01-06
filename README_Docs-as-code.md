# Docs-as-Code
Teams using Markdown as the source format can use this MkDocs based template to generate HCL SW docs

# Prerequisites
## Installing MkDocs
https://www.mkdocs.org/user-guide/installation/
## Installing Material for MkDocs
https://squidfunk.github.io/mkdocs-material/getting-started/

**Note:** To check whether MkDocs is installed, run this command:
> mkdocs -V

MkDocs comes with a built-in dev-server that lets you preview your documentation as you work on it. Make sure you're in the same directory as the mkdocs.yml configuration file, and then start the server by running the mkdocs serve command.

You can see the default home page in the browser with this URL:
http://127.0.0.1:8000

# Configuration file
*site_name* - Give full product name. Appears below the header and besides the product logo
*site_description* - Give brief description about the site. Use appropriate keywords for a search engine to find the site easily.
*site_url* - Change product-name with the name of the product. Do not use spaces.

*extra:*
*social* - Do not change the GitHub icon and link 
*version* - Comment it with a # symbol if you do not need a version switcher.
*analytics* - Do not uncomment it till we implement the cookie consent banner.

*repo_url* - Give the URL to your public GitHub repository
*repo_name* - Give a name to your repository

*nav* - 
-   Indentation and formatting (usage of dash, colon, etc.) are key to navigation. 
-   First-level topics show up in the top navigation. Be prudent about the number of first-level topics. It's a good idea to use Personas as the first-level topics. Too many topics at the top might make the site less user-friendly.
-   By default, in MkDocs, if there is a child topic, the parent node must not contain a topic in the nav. If you want the parent node to have a topic, use *section index*. (https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/?h=#section-index-pages).

# Adding versions
Material for MkDocs uses mike for the version function. By default, this function is enabled in mkdocs.yml.

To view the version dropdown on your site:
1. Create one branch in Git to keep all of your output (HTML) documentation. 
2. Ensure that you orgnanize the documentation for each version in a folder. The name of the folder should be the version name. 
3. Add this [JSON file](https://github01.hclpnp.com/UA-PNP/Docs-as-Code/blob/develop/docs/assets/versions.json) to the root of the branch and add the version numbers in the JSON file.

# Material icons
We are using Material Icons syntax in PyMdown Extensions. For example, the notation :material-server-network:{ .lg .middle } applies:
:material-server-network: → The server-network icon from Material Design Icons.
.lg → Large icon size.
.middle → Vertical alignment to the middle.
You can explore more about Material Icons styling in [MkDocForge's guide](https://mdevpro78.github.io/mkdocforge/material-icons-guide/) and check out the [Material Design Icons](https://pictogrammers.com/library/mdi/).


# What's new in June2025 release
https://github01.hclpnp.com/UA-PNP/Docs-as-Code/releases/tag/v.June2025

- Content templates 

  Content types (Tutorials, How-to, Explanations (Concepts) and Reference) follow the Diataxis framework. To provide robust templates and guidance for these content types, the Good Docs Project was used. Additional templates from the Good Docs Project were also provided. You can read the style guide for more information about these templates.  

- Home page

  The home page follows the latest design guidance for Digital Experience. Banners, logos, and favicons for each product are provided in the theme_overrides folder. 

- Header and Footer fixes

  The header and footer was made to be similar to the WebHelp template. 

- Giscus commenting system 

  The Giscus commenting system was added. 

- Banners

  The banner text and background color was updated to be the same as the WebHelp template. 


   

