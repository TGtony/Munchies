$(document).ready(function () {

    $('#submit').click(function (event) {
        var toggle_indexes = [];
        var query_string = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        $('.highlight').each(function (i, obj) {
            toggle_indexes.push($(this).attr('value'));
        });
        $.each(toggle_indexes, function(i, obj){
            query_string = replaceAt(query_string, parseInt(toggle_indexes[i]), "1");
        })
        alert(query_string);
        $('#query').val(query_string);
    });

});

function replaceAt(s, n, t) {
    return s.substring(0, n) + t + s.substring(n+1);
}