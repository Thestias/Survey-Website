window.onload = function () {
    let value;
    // THIS SENDS A POST TO CREARE_SURVEY/ADD/<SURVEY_ID> TO UPDATE SURVEYS WITH QUESTIONS AND OPTIONS 
    function update_survey() {
        value = JSON.parse(document.getElementById('survey_id').textContent);
        $('#form').submit(function (event) {
            let data = $('#form').serialize()
            $.ajax({
                type: "POST",
                url: "add/" + value, // Page to send the Data!
                dataType: "json",
                data: data,
            })
                .done(function (data) {
                    $('#after_submit').html('<p class="text-xl md:text-lg font-mono font-bold text-green-600 ">Success!</p>')
                    console.log(data)
                })
                .fail(function (data) {
                    $('#after_submit').html('<p class="text-xl md:text-lg font-mono font-bold text-red-600 ">Error!</p>')
                })
            event.preventDefault();
        })
    } // ENDS update_survey
    update_survey()
} // ENDS ONLOAD