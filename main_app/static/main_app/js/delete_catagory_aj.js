/**
 * Created by sajid on 11/15/2015.
 */
 $(document).ready(function() {
        $('#YOUR_FORM').submit(function() { // catch the form's submit event
            $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: $(this).attr('action'), // the file to call
                success: function(response) {
                    $('#DIV_CONTAINING_FORM').html(response);
                }
            });
            return false;
        });
    });