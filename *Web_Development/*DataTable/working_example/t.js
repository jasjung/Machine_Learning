$(document).ready(function () {
  $('#dtBasicExample').DataTable(
  	{"order": [[ 1, "desc" ]]});
  $('.dataTables_length').addClass('bs-select');
});

$(document).ready(function () {
  $('#table_id').DataTable();
  $('.dataTables_length').addClass('bs-select');
});

function myFunction() {
  alert("Hello! I am an alert box!");
}