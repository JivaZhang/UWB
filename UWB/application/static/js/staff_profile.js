function executeQueryForAll() {
  $.ajax({
    url: '/uwb/all_json/',
    success: function(data) {
        collected_data = jQuery.parseJSON(data)['collected_data'];
        $('#stage').html('<p> Dane dla użytkownika: ' + collected_data.lecturer_name  + ' </p>');
        for (i = 0; i < collected_data.lecturer_data.length; i++) {
            $('#stage').append('<p> Dane dla zajęć: '
             + collected_data.lecturer_data[i].classes_name + ' </p>');
            for (j = 0; j < collected_data.lecturer_data[i].classes_data.length; j++) {
                student_data = collected_data.lecturer_data[i].classes_data[j]
                if(student_data.attendance) {
                    $('#stage').append('<p> ' + (j + 1) + '. Student: ' +
                student_data.first_name + ' ' + student_data.last_name + ' ' + 
                student_data.index_number + ' ' + student_data.attendance_date + 
                '<font color="green"> Obecny </font>' +' </p>');
                }
                else {
                    $('#stage').append('<p> ' + (j + 1) + '. Student: ' +
                student_data.first_name + ' ' + student_data.last_name + ' ' + 
                student_data.index_number + ' ' + student_data.attendance_date + 
                '<font color="red"> Nieobecny </font>' +' </p>');
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
        $('#stage').html('<p> Dane dla użytkownika: ' + collected_data.lecturer_name  + ' </p>');
        for (i = 0; i < collected_data.lecturer_data.length; i++) {
            $('#stage').append('<p> Dane dla zajęć: '
             + collected_data.lecturer_data[i].classes_name + ' </p>');
            for (j = 0; j < collected_data.lecturer_data[i].classes_data.length; j++) {
                student_data = collected_data.lecturer_data[i].classes_data[j]
                if(student_data.attendance) {
                    $('#stage').append('<p> ' + (j + 1) + '. Student: ' +
                student_data.first_name + ' ' + student_data.last_name + ' ' + 
                student_data.index_number + ' ' + student_data.attendance_date + 
                '<font color="green"> Obecny </font>' +' </p>');
                }
                else {
                    $('#stage').append('<p> ' + (j + 1) + '. Student: ' +
                student_data.first_name + ' ' + student_data.last_name + ' ' + 
                student_data.index_number + ' ' + student_data.attendance_date + 
                '<font color="red"> Nieobecny </font>' +' </p>');
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