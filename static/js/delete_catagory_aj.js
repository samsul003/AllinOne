/**
 * Created by sajid on 11/15/2015.
 */
 $(document).ready(function() {
        $('.delete-form').submit(function() { // catch the form's submit event
            $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: $(this).attr('action'), // the file to call
                success: function(response) {
                    $(this).hide();
                    alert("Hello");
                }
            });
            return false;
        });
    });