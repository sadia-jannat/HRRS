// Product Review Save
$("#addForm").submit(function(e) {


    $.ajax({
        fe: $(this).serialize(),
        method: $(this).attr('method'),
        url: $(this).attr('action'),

        dataType: 'json',
        success: function(res) {
            if (res.bool == true) {

                $(".ajaxRes").html('Data has been added.');
                $("#reset").trigger('click');

                var_html = '<blockquote class="blockquote text-right">';
                _html += '<h3> +res.fe.info_review+ </h3>';
                _html += '<cite title="Source Title">';

                for (var i = 1; i <= res.fe.info_rate; i++) {
                    _html += '<i class="fa fa-star text-warning"></i>';
                }

                _html += '</cite>';
                _html += '</blockquote>';
                _html += '<hr />';


                //hide no data and first data ok
                $(".no-data").hide();

                //prepend fe
                $(".review-list").prepend(_html);

                //avg rate
                $(".avg-rate").text(res.fe.avg_reviewfetch.toFixed(1))


            }
        }
    });
    e.preventDefault();
});
// End
// End