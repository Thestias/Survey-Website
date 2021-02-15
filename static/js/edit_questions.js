window.onload = function () {
    let value;
    // THIS SENDS A POST TO CREARE_SURVEY/ADD/<SURVEY_ID> TO UPDATE SURVEYS WITH QUESTIONS AND OPTIONS 
    function update_survey() {
        value = JSON.parse(document.getElementById('survey_id').textContent);
        $('#form').submit(function (event) {
            let data = $('#form').serialize()
            $.ajax({
                type: "POST",
                url: "submit/", // Page to send the Data!
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

    update_survey()

    let form = document.querySelector('#form')

    // THESE TWO LISTENERS ADD AND REMOVE QUESTIONS
    form.querySelector('#question-add').addEventListener('click', function () {
        // TODO : LIMIT FOR ADDING QUESTIONS
        create_question_form()
    })

    form.querySelector('#question-remove').addEventListener('click', function () {
        let question_forms = document.querySelectorAll('.question-wrapper')
        if (question_forms.length != 1) {
            question_forms[question_forms.length - 1].remove()
            document.querySelector('#id_question_set-TOTAL_FORMS').setAttribute('value', document.querySelectorAll('.question-wrapper').length)
        }
    })

    form.querySelectorAll('#option-add').forEach(function (e) {
        e.addEventListener('click', function () {
            add_option(e)
        })
    })

    function create_question_form() {
        /*
        * This function clones a empty form found in the HTML and adds it to the questions form
        */
        let empty_form = document.querySelector('#empty-form').cloneNode(true)
        empty_form.classList.remove('hidden')
        empty_form.classList.add('question-wrapper')
        empty_form.removeAttribute('id')

        let empty_question_form = empty_form.querySelector('.question-empty-form')
        let ammount_questions = document.querySelectorAll('.question-wrapper')

        empty_question_form.innerHTML = empty_question_form.innerHTML.replaceAll('__prefix__', ammount_questions.length)
        form.querySelector('#id_question_set-TOTAL_FORMS').setAttribute('value', ammount_questions.length + 1)

        let empty_option_form = empty_form.querySelector('.empty-option-form')

        // The -0- is for the Question and __prefix__ for the amm of option, the question replace should be always before the option replace
        empty_option_form.innerHTML = empty_option_form.innerHTML.replaceAll('-0-', '-' + (ammount_questions.length) + '-')
        empty_option_form.innerHTML = empty_option_form.innerHTML.replaceAll('__prefix__', '0')

        empty_option_form.querySelector('#' + 'id_option-question_set-' + ammount_questions.length + '-option_set-TOTAL_FORMS').setAttribute('value', '1')
        empty_option_form.querySelector('#' + 'id_option-question_set-' + ammount_questions.length + '-option_set-INITIAL_FORMS').setAttribute('value', '0')

        empty_form.querySelector('#option-add').addEventListener('click', function () {
            add_option(empty_form.querySelector('#option-add'))
        })

        // empty_form.querySelector('#option-remove').addEventListener('click', function () {
        //     remove_option(empty_form.querySelector('#option-remove'))
        // })

        form.querySelector('#question-add').insertAdjacentElement('beforebegin', empty_form)

    }


    // OPTION CREATION HANDLING

    function add_option(option_clicked_element) {
        // Holds the value of the ID of the first INPUT in the MANAGEMENTFORM Attribute {STRING}
        let array_id_management_form = (option_clicked_element.parentNode.querySelector('input').getAttribute('id'))
        let question_id_value = array_id_management_form.split('-')[2]

        let empty_option = document.querySelector('#empty-form').querySelector('.option').cloneNode(true)

        let amm_options = option_clicked_element.parentNode.querySelectorAll('.option').length

        empty_option.innerHTML = empty_option.innerHTML.replaceAll('-0-', '-' + question_id_value + '-')
        empty_option.innerHTML = empty_option.innerHTML.replaceAll('__prefix__', amm_options)

        document.querySelector('#' + array_id_management_form).setAttribute('value', amm_options + 1)

        option_clicked_element.insertAdjacentElement('beforebegin', empty_option)
    }


}