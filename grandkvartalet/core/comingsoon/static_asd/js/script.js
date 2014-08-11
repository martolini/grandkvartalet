$(function() {

    var note = $('#note')
    ////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////

    var year = 2014; //enter YEAR here//
    var month = 7; //enter MONTH here - ex. 5 for May//
    var date = 21; //enter DATE here//
    var hour = 0; //enter HOUR here; 24hour format; ex. 20 for 8PM//
    var min = 0; //enter MINUTES here//
    var sec = 0; //enter SECONDS here//

    ////////////////////////////////////////////////////////////////////////		
    ////////////////////////////////////////////////////////////////////////

    ts = new Date(year, month - 1, date, hour, min, sec),
    newYear = true;

    if ((new Date()) > ts) {
        // Notice the *1000 at the end - time must be in milliseconds
        ts = (new Date()).getTime() + 10 * 24 * 60 * 60 * 1000;
        newYear = false;
    }

    $('#countdown').countdown({
        timestamp: ts,
        callback: function(days, hours, minutes, seconds) {

            var message = "";

            message += days + " day" + (days == 1 ? '' : 's') + ", ";
            message += hours + " hour" + (hours == 1 ? '' : 's') + ", ";
            message += minutes + " minute" + (minutes == 1 ? '' : 's') + " and ";
            message += seconds + " second" + (seconds == 1 ? '' : 's') + " <br />";

            if (newYear) {
                message += "";
            } else {
                message += "";
            }

            note.html(message);
        }
    });

});