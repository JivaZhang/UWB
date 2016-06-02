function executeQuery() {
  $.ajax({
    url: '/uwb/profile_json/',
    success: function(data) {
        collected_data = jQuery.parseJSON(data)['collected_data'];

        $('#stage').html('<p> Dane dla użytkownika: ' + collected_data.student_name  + ' </p>' + '<table id="table" class="table table-striped table-bordered" cellspacing="0" width="100%"><thead><tr><th>Kurs</th><th>Prowadzący</th><th>Data</th><th>Obecność</th></tr></thead><tbody>');
        for (i = 0; i < collected_data.student_data.length; i++) {

            if(collected_data.student_data[i].attendance) {

                $('#stage').append(
		'<tr><td>' + collected_data.student_data[i].classes_name + '</td><td>' + collected_data.student_data[i].lecturer_name + '</td><td>' + collected_data.student_data[i].attendance_date + '</td><td>' + '<font color="green"> Obecny </font>' + '</td></tr>')

            }
            else {
                $('#stage').append(
		'<tr><td>' + collected_data.student_data[i].classes_name + '</td><td>' + collected_data.student_data[i].lecturer_name + '</td><td>' + collected_data.student_data[i].attendance_date + '</td><td>' + '<font color="red"> Nieobecny </font>' + '</td></tr>')
            }
        }
	$('#stage').append('</tbody></table>');

    }
  });
  setTimeout(executeQuery, 5000); 
}

$(document).ready(function() {
    executeQuery();
});
