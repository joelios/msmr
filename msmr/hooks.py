# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "msmr"
app_title = "msmr"
app_publisher = "Joel Mesmer"
app_description = "all about msmr.ch"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "joel@msmr.ch"
app_license = "MIT"

# Includes in <head>
# ------------------
base_template_path = "/msmr/templates/base.html"
# include js, css files in header of desk.html
# app_include_css = "/assets/msmr/css/msmr.css"
# app_include_js = "/assets/msmr/js/msmr.js"

# include js, css files in header of web template
web_include_css = "/assets/msmr/css/msmr.css"
web_include_js = "/assets/msmr/js/msmr.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "msmr"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "msmr.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "msmr.install.before_install"
# after_install = "msmr.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "msmr.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"msmr.tasks.all"
# 	],
# 	"daily": [
# 		"msmr.tasks.daily"
# 	],
# 	"hourly": [
# 		"msmr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"msmr.tasks.weekly"
# 	]
# 	"monthly": [
# 		"msmr.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "msmr.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "msmr.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "msmr.task.get_dashboard_data"
# }

