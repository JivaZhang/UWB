function executeQueryForAll() {
  $.ajax({
    url: '/uwb/all_json/',
    success: function(data) {
        collected_data = jQuery.parseJSON(data)['collected_data'];

        $('#stage').html('<h4> Dane dla użytkownika: <b>' + collected_data.lecturer_name  + '</b></h4>');

        for (i = 0; i < collected_data.lecturer_data.length; i++) {

            $('#stage').append('<h4> Dane dla zajęć: <b>' + collected_data.lecturer_data[i].classes_name + '</b></h4>')
	    $('#stage').append('<table id="table" class="table table-condensed table-bordered" width="100%"><thead><tr><th>#</th><th>Imię</th><th>Nazwisko</th><th>Nr Indeksu</th><th>Data</th><th>Obecność</th></tr></thead><tbody></tbody></table>');

            for (j = 0; j < collected_data.lecturer_data[i].classes_data.length; j++) {
                student_data = collected_data.lecturer_data[i].classes_data[j]

                if(student_data.attendance) {
		console
                    $('#table').append('<tr><td>' + (j + 1) + '</td><td>' + student_data.first_name + '</td><td>' + student_data.last_name + '</td><td>' + student_data.index_number + '</td><td>' + student_data.attendance_date + '</td><td>' + '<font color="green"> Obecny </font>' + '</td></tr>');
                }

                else {
                    $('#table').append('<tr><td>' + (j + 1) + '</td><td>' + student_data.first_name + '</td><td>' + student_data.last_name + '</td><td>' + student_data.index_number + '</td><td>' + student_data.attendance_date + '</td><td>' + '<font color="red"> Nieobecny </font>' + '</td></tr>');
                }
            }
        }
    }
  });
  setTimeout(executeQueryForAll, 5000); 
}

function executeQueryForProfile() {
  $.ajax({
    url: '/uwb/profile_json/',
    success: function(data) {
        collected_data = jQuery.parseJSON(data)['collected_data'];

        $('#stage').html('<h4> Dane dla użytkownika: <b>' + collected_data.lecturer_name  + '</b></h4>');

        for (i = 0; i < collected_data.lecturer_data.length; i++) {

            $('#stage').append('<h4> Dane dla zajęć: <b>' + collected_data.lecturer_data[i].classes_name + '</b></h4>')
	    $('#stage').append('<table id="table" class="table table-condensed table-bordered" width="100%"><thead><tr><th>#</th><th>Imię</th><th>Nazwisko</th><th>Nr Indeksu</th><th>Data</th><th>Obecność</th></tr></thead><tbody></tbody></table>');

            for (j = 0; j < collected_data.lecturer_data[i].classes_data.length; j++) {
                student_data = collected_data.lecturer_data[i].classes_data[j]

                if(student_data.attendance) {
		console
                    $('#table').append('<tr><td>' + (j + 1) + '</td><td>' + student_data.first_name + '</td><td>' + student_data.last_name + '</td><td>' + student_data.index_number + '</td><td>' + student_data.attendance_date + '</td><td>' + '<font color="green"> Obecny </font>' + '</td></tr>');
                }

                else {
                    $('#table').append('<tr><td>' + (j + 1) + '</td><td>' + student_data.first_name + '</td><td>' + student_data.last_name + '</td><td>' + student_data.index_number + '</td><td>' + student_data.attendance_date + '</td><td>' + '<font color="red"> Nieobecny </font>' + '</td></tr>');
                }
            }
        }
    }
  });
  setTimeout(executeQueryForProfile, 5000); 
}

$(document).ready(function() {
    if(window.location.pathname.indexOf('all') > -1) {
        executeQueryForAll();
    }
    else {
        executeQueryForProfile();
    }
});
