# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
import six
import json

@frappe.whitelist(allow_guest=True)
def create_idee(anlagedaten):
    if isinstance(anlagedaten, six.string_types):
        anlagedaten = json.loads(anlagedaten)
    
    new_idee = frappe.get_doc({
        'doctype': 'Ideen Briefkasten',
        'vor_nachnamen': anlagedaten['vor_nachnamen'] if anlagedaten['vor_nachnamen'] else None,
        'email': anlagedaten['email'] if anlagedaten['email'] else None,
        'idee': anlagedaten['idee'] if anlagedaten['idee'] else None
    }).insert()
    
    return
