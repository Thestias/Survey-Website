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

    let empty_form;
    let total_forms_id;
    function add_option() {
        document.querySelectorAll('#option-add').forEach(function (e) {
            e.addEventListener('click', function () {
                empty_form = e.parentNode.querySelector('.empty-option')
                total_forms_id = empty_form.firstChild.getAttribute('for').replace('-__prefix__-option', '-TOTAL_FORMS')
                empty_form = empty_form.cloneNode(true)
                empty_form.classList.remove('hidden')
                empty_form.classList.remove('empty-option')
                empty_form.classList.add('option-wrapper')
                amm_inputs = e.parentNode.querySelectorAll('input').length / 4 - 1

                empty_form.innerHTML = empty_form.innerHTML.replaceAll('__prefix__', amm_inputs)

                empty_form.querySelectorAll('label').forEach(function (e) {
                    e.classList = 'inline-block text-xl font-mono font-bold text-purple-700 e mr-8'
                })
                e.insertAdjacentElement('beforebegin', empty_form)
                document.querySelector('#' + total_forms_id).setAttribute('value', amm_inputs + 1)
            })
        })
    }

    function remove_option() {
        document.querySelectorAll('#option-remove').forEach(function (e) {
            e.addEventListener('click', function () {
                let option_wrappers = e.parentNode.querySelectorAll('.option-wrapper')

                if (option_wrappers.length != 1) {

                    total_forms_id = e.parentNode.querySelector('.empty-option').firstChild.getAttribute('for').replace('-__prefix__-option', '-TOTAL_FORMS')
                    amm_inputs = e.parentNode.querySelectorAll('.option-wrapper').length - 1

                    let check_delete = e.parentNode.querySelector('.empty-option').firstChild.getAttribute('for').replace('-__prefix__-option', '-' + (amm_inputs) + '-DELETE')
                    console.log(check_delete)
                    document.querySelector('#' + check_delete).checked = true
                    // document.querySelector('#' + total_forms_id).setAttribute('value', amm_inputs)
                    option_wrappers[option_wrappers.length - 1].classList = 'hidden'


                }

            })
        })
    }

    update_survey()
    add_option()
    remove_option()
} // ENDS ONLOAD