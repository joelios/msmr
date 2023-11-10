frappe.pages['vorratsliste'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Vorratsliste',
		single_column: true
	});
    let $btn = page.set_primary_action('New', () => new_scan(), 'octicon octicon-plus')
}


function new_scan() {
    new frappe.barcode.scan_barcode();
}
