function executeQuery() {
  $.ajax({
    url: '/uwb/profile_json/',
    success: function(data) {
        collected_data = jQuery.parseJSON(data)['collected_data'];
        $('#stage').html('<p> Dane dla użytkownika: ' + collected_data.student_name  + ' </p>');
        for (i = 0; i < collected_data.student_data.length; i++) {
            if(collected_data.student_data[i].attendance) {
                $('#stage').append('<p> ' + collected_data.student_data[i].classes_name + ' ' +
                    collected_data.student_data[i].lecturer_name + ' ' +
                    collected_data.student_data[i].attendance_date + ' ' +
                    '<font color="green"> Obecny </font>' + '</p> ')
            }
            else {
                $('#stage').append('<p> ' + collected_data.student_data[i].classes_name + ' ' +
                    collected_data.student_data[i].lecturer_name + ' ' +
                    collected_data.student_data[i].attendance_date + ' ' +
                    '<font color="red"> Nieobecny </font>' + '</p> ')
            }
        }
    }
  });
  setTimeout(executeQuery, 5000); 
}

$(document).ready(function() {
    executeQuery();
});