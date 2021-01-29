window.onload = function () {
    let add_question_btn = document.querySelector('#add_question')
    let parentArticle = add_question_btn.parentNode
    let remove_question_btn = document.querySelector('#remove_question')
    AMMOUNT_OF_QUESTIONS = (document.querySelectorAll('.question-wrapper').length + 1).toString()

    /* CREATING NESSESARY ELEMENTS */

    /* Creating Question Div Wrapper */
    function question_wrapper_creation() {
        let question_wrapper = document.createElement('div');
        question_wrapper.setAttribute('id', 'question_' + AMMOUNT_OF_QUESTIONS)
        question_wrapper.classList.add('question-wrapper', 'mt-4')

        return question_wrapper
    }

    function label_creation(type_label, inner_text, css_classes = 'NoClasses') {
        /*
        * Creates a html label
        * @param {STRING} type_label If the label is a "question" type
        * @param {STRING} inner_text The text of the label
        * @param {STRING} css_classes A string of coma separated CSS Classes
        * @return {Object}  Returns the new Label Element.
        */
        let label = document.createElement('label');
        label.classList.add('custom_label_text_one')
        if (css_classes != 'NoClasses') {
            css_classes = css_classes.split(' ')
            label.classList.add(...css_classes)
        }

        if (type_label === 'question') {
            label.setAttribute('for', 'question_' + AMMOUNT_OF_QUESTIONS)
        } else if (type_label === 'OPTION') {
            label.classList.add('label-no-style')
        };
        label.innerText = inner_text;

        return label
    }

    function input_creation(type_input, css_classes = 'NoClasses') {
        /*
        * Creates a html input
        * @param {STRING} type_input A choice between QUESTION and OPTION.
        * @param {STRING} css_classes A string of coma separated CSS Classes
        * @return {Object}  The Input Element
        */
        let input = document.createElement('input')
        input.classList.add('custom_input_one')
        if (css_classes != 'NoClasses') {
            css_classes = css_classes.split(' ')
            input.classList.add(...css_classes)
        }
        input.setAttribute('type', 'text')
        if (type_input === 'QUESTION') {
            input.required = true
            input.setAttribute('name', 'question_' + AMMOUNT_OF_QUESTIONS)
        } else if (type_input === 'OPTION') {
            input.classList.add('option-no-style')
            input.required = true
            input.setAttribute('name', question_wrapper.getAttribute('id'))
        }

        return input

    }

    function option_button(type_button) {
        let option_btn = document.createElement('div')
        option_btn.classList.add('inline-block', 'custom_button_one', 'ml-16') // These are general styles
        if (type_button === 'REMOVE') {
            option_btn.classList.add('custom_button_one_remove', 'w-44')
            option_btn.innerText = 'Remove Option'
            option_btn.addEventListener('click', function () {
                let find_input_options = option_btn.parentNode.querySelectorAll('.option-no-style')
                let find_label_options = option_btn.parentNode.querySelectorAll('.label-no-style')
                find_label_options[find_label_options.length - 1].remove()
                find_input_options[find_input_options.length - 1].remove()
            })
        } else if (type_button === 'ADD') {
            option_btn.classList.add('custom_button_one_add', 'w-36')
            option_btn.innerText = 'Add Option'
            option_btn.addEventListener('click', function () {
                option_btn.insertAdjacentElement('beforebegin', label_creation('OPTION', 'Option', 'mr-9'))
                option_btn.insertAdjacentElement('beforebegin', input_creation('OPTION'))
            })
        }
        return option_btn
    }

    add_question_btn.addEventListener('click', function () {

        /* Creating Separator */
        let question_separator = document.createElement('hr')

        /* PLACING ELEMENTS */
        question_wrapper = question_wrapper_creation()
        question_wrapper.insertAdjacentElement('beforeend', label_creation('QUESTION', 'Question', 'mr-4'))
        question_wrapper.insertAdjacentElement('beforeend', input_creation('QUESTION'))
        question_wrapper.insertAdjacentElement('beforeend', option_button('ADD'))
        question_wrapper.insertAdjacentElement('beforeend', option_button('REMOVE'))
        question_wrapper.insertAdjacentElement('beforeend', question_separator)
        parentArticle.insertBefore(question_wrapper, add_question_btn)
    })

    let all_questions;
    remove_question_btn.addEventListener('click', function () {
        all_questions = document.querySelectorAll('.question-wrapper')
        if (all_questions.length != 1) {
            all_questions[all_questions.length - 1].remove()
        }
    })


    /* Creating Separator */
    let question_separator = document.createElement('hr')

    let question_wrapper = question_wrapper_creation()
    /* PLACING ELEMENTS */
    question_wrapper.insertAdjacentElement('beforeend', label_creation('QUESTION', 'Question', 'mr-4'))
    question_wrapper.insertAdjacentElement('beforeend', input_creation('QUESTION'))
    question_wrapper.insertAdjacentElement('beforeend', option_button('ADD'))
    question_wrapper.insertAdjacentElement('beforeend', option_button('REMOVE'))
    question_wrapper.insertAdjacentElement('beforeend', question_separator)
    parentArticle.insertBefore(question_wrapper, add_question_btn)

}