$(function() {
    $('#btnSignUp').click(function() {

        $.ajax({
            url: '/mountUp',
            data: $('form').serialize(),
            type: 'GET',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});