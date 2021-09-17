"use strict";
var DatatablesDataSourceHtml = function() {

	var initTable1 = function() {
		var table = $('#k_table_1');

		// begin first table
		table.DataTable({
			responsive: true,
			destroy: true,
			deferRender: true,
			ajax: {
				url: window.location.pathname,
				type: 'POST',
				data: {
					'action': 'searchdata'
				},
				dataSrc: ""
			},
			"oLanguage": {
            "oPaginate": { "sPrevious": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-arrow-left"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>', "sNext": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-arrow-right"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>' },
            "sInfo": "Mostrando pág. _PAGE_ de _PAGES_",
            "sSearch": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-search"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
            "sSearchPlaceholder": "Buscar...",
            "sLengthMenu": "Filtro :  _MENU_",
        },
			columns: [
				{ "data": "id"},
				{ "data": "name_client_1"},
				{ "data": "last_names_cliente"},
				{ "data": "identification"},
				{ "data": "email"},
				{ "data": "mobile"},
				{ "data": "city.name"},
				{ "data": "city"},
			],
			columnDefs: [
				{
					targets: -1,
					title: 'Opciones',
					orderable: false,
					render: function (data, type, row) {
						var buttonss = '<a href="/erp/contact/edit/'+row.id+'/" class="btn btn-sm btn-clean btn-icon btn-icon-md" title="Editar">\n' +
							'                    <i class="la la-edit"></i>\n' +
							'                </a>\n' +
							'                <span class="dropdown">\n' +
							'                    <a href="#" class="btn btn-sm btn-clean btn-icon btn-icon-md" data-toggle="dropdown" aria-expanded="true">\n' +
							'                        <i class="la la-ellipsis-h"></i>\n' +
							'                    </a>\n' +
							'                    <div class="dropdown-menu dropdown-menu-right">\n' +
							'                        <a class="dropdown-item" href="#"><i class="la la-eye"></i> Ver</a>\n' +
							'                        <a class="dropdown-item" href="/erp/contact/delete/'+row.id+'/"><i class="la la-trash"></i> Eliminar</a>\n' +
							'                    </div>\n' +
							'                </span>';
						return buttonss;
					}
				},
			],
			initComplete: function(settings, json) {

			}
		});

	};

	return {

		//main function to initiate the module
		init: function() {
			initTable1();
		},

	};

}();

jQuery(document).ready(function() {
	DatatablesDataSourceHtml.init();
});