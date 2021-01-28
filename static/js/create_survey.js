window.onload = function () {
    let ammount_questions = (document.querySelectorAll('.question-wrapper').length + 1).toString()
    let add_question_btn = document.querySelector('#add_question')
    let parentArticle = add_question_btn.parentNode

    add_question_btn.addEventListener('click', function () {
        ammount_questions = (document.querySelectorAll('.question-wrapper').length + 1).toString()

        /* CREATING NESSESARY ELEMENTS */

        /* Creating Question Div Wrapper */
        let question_wrapper = document.createElement('div');
        question_wrapper.classList.add('question-wrapper', 'mt-4')

        /* Creating Label */
        let question_label = document.createElement('label')
        question_label.classList.add('custom_label_text_one', 'mr-4')
        question_label.setAttribute('for', 'question_' + ammount_questions)
        question_label.innerText = 'Question'

        /* Creating Input */
        let question_input = document.createElement('input')
        question_input.classList.add('custom_input_one')
        question_input.setAttribute('id', 'question_' + ammount_questions)
        question_input.setAttribute('type', 'text')
        question_input.setAttribute('name', 'question_' + ammount_questions)

        /* Creating Add Option Button */
        let question_op_button = document.createElement('div')
        question_op_button.classList.add('custom_button_one', 'custom_button_one_add', 'ml-16', 'w-36')
        question_op_button.innerText = 'Add Option'

        /* Creating Separator */
        let question_separator = document.createElement('hr')

        /* PLACING ELEMENTS */
        question_wrapper.insertAdjacentElement('beforeend', question_label)
        question_wrapper.insertAdjacentElement('beforeend', question_input)
        question_wrapper.insertAdjacentElement('beforeend', question_op_button)
        question_wrapper.insertAdjacentElement('beforeend', question_separator)
        parentArticle.insertBefore(question_wrapper, add_question_btn)




    })
}