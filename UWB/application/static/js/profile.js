function executeQuery() {
  $.ajax({
    url: '/uwb/profile_json/',
    success: function(data) {
        collected_data = jQuery.parseJSON(data)['collected_data'];

        $('#stage').html('<h4> Dane dla użytkownika: <b>' + collected_data.student_name  + '</b><h4>')
        $('#stage').append('<table id="table" class="table table-condensed table-bordered" width="100%"><thead><tr><th>Kurs</th><th>Prowadzący</th><th>Data</th><th>Obecność</th></tr></thead><tbody></tbody></table>');

        for (i = 0; i < collected_data.student_data.length; i++) {

            if(collected_data.student_data[i].attendance) {
                $('#table').append('<tr><td>' + collected_data.student_data[i].classes_name + '</td><td>' + collected_data.student_data[i].lecturer_name + '</td><td>' + collected_data.student_data[i].attendance_date + '</td><td>' + '<font color="green"> Obecny </font>' + '</td></tr>');
            }

            else {
                $('#table').append('<tr><td>' + collected_data.student_data[i].classes_name + '</td><td>' + collected_data.student_data[i].lecturer_name + '</td><td>' + collected_data.student_data[i].attendance_date + '</td><td>' + '<font color="red"> Nieobecny </font>' + '</td></tr>');
            }
        }
    }
  });
  setTimeout(executeQuery, 5000); 
}

$(document).ready(function() {
    executeQuery();
});
