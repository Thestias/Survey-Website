window.onload = function () {
    let value;
    // THIS SENDS A POST TO CREARE_SURVEY/ADD/<SURVEY_ID> TO UPDATE SURVEYS WITH QUESTIONS AND OPTIONS 
    function update_survey() {
        value = JSON.parse(document.getElementById('survey_id').textContent);
        $('#form').submit(function (event) {
            let data = $('#form').serialize()
            $.ajax({
                type: "POST",
                url: "submit/" + value, // Page to send the Data!
                dataType: "json",
                data: data,
            })
                .done(function (data) {
                    $('#after_submit').html('<p class="text-xl md:text-lg font-mono font-bold text-green-600 ">Success!</p>')
                    console.log(data)
                })
                .fail(function (data) {
                    $('#after_submit').html('<p class="text-xl md:text-lg font-mono font-bold text-red-600 ">Error!</p>')
                    console.log(data)
                })
            event.preventDefault();
        })
    } // ENDS update_survey

    let question_forms; // THIS ONE HAS ALL THE QUESTIONS WRAPPERS NEEDED TO INCREASE AMMOUNT OF FORMS ALLOWED
    let add_question = document.querySelector('#question-add')
    let remove_question = document.querySelector('#question-remove')
    let new_form;
    let new_amm_forms;

    let amm_forms_allowed = document.querySelector('#id_question_set-TOTAL_FORMS')

    add_question.addEventListener('click', add_question_form)

    remove_question.addEventListener('click', remove_question_form)

    function add_question_form() {
        question_forms = document.querySelectorAll('.question-wrapper')
        new_amm_forms = question_forms.length + 1
        amm_forms_allowed.setAttribute('value', new_amm_forms)
        new_form = document.querySelector('#empty-form').cloneNode(true)
        new_form.classList = 'question-wrapper'
        new_form.setAttribute('id', '')


        // new_form.innerHTML = new_form.innerHTML.replaceAll('')
        new_form.innerHTML = new_form.innerHTML.replaceAll('__prefix__', new_amm_forms)

        add_question.insertAdjacentElement('beforebegin', new_form)
    }

    function remove_question_form() {
        question_forms = document.querySelectorAll('.question-wrapper')
        if (question_forms.length != 1) {
            question_forms[question_forms.length - 1].remove()
        }
    }

    update_survey()
} // ENDS ONLOAD