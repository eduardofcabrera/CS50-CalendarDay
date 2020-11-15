document.addEventListener('DOMContentLoaded', function() {

    buttonsEvents()
    TAAEvents()
    createTAAEvents()

})

function createTAAEvents() {
    let create_button = document.querySelector('#create-image')
    create_button.addEventListener('click', function() {
        removeTAA()
        appearCreateTAA()
    })
}

function removeTAA() {
    let TAAElement = document.querySelector('#TAAElement')
    TAAElement.style.display = 'none'
}

function appearCreateTAA() {
    let createTAA = getCreateDiv()

    if (createTAA.style.display === 'none' || !createTAA.style.display ) {
        createTAA.style.display = 'block'
    } else {
        createTAA.style.display = 'none'
    }


    
}

function buttonsEvents() {
    calendarEvents()
    typeEvents()
}

function calendarEvents() {
    
    let buttonDay = getButtonDay()
    let buttonWeek = getButtonWeek()
    let buttonMonth = getButtonMonth()

    buttonDay.addEventListener('click', buttonDayClick)
    buttonWeek.addEventListener('click', buttonWeekClick)
    buttonMonth.addEventListener('click', buttonMonthClick)
}

function buttonDayClick() {

    let buttonId = 0
    changeClassButton(buttonId)
    changeClassDivCalendar(buttonId)

}

function buttonWeekClick() {

    let buttonId = 1
    changeClassButton(buttonId)
    changeClassDivCalendar(buttonId)
    
}

function buttonMonthClick() {

    let buttonId = 2
    changeClassButton(buttonId)
    changeClassDivCalendar(buttonId)
    
}

function changeClassButton(buttonId) {
    let butttons = getArrayButtonCalendar()
    for(let i = 0; i < butttons.length; i++) {
        if(i === buttonId) {
            butttons[i].className = 'button-active'
        } else {
            butttons[i].className = 'button'
        }
    }
}

function getArrayButtonCalendar() {

    let buttonDay = getButtonDay()
    let buttonWeek = getButtonWeek()
    let buttonMonth = getButtonMonth()

    let arrayButton = []
    arrayButton.push(buttonDay)
    arrayButton.push(buttonWeek)
    arrayButton.push(buttonMonth)

    return arrayButton

}

function changeClassDivCalendar(buttonId) {

    let divs = document.querySelectorAll(".place")
    for(let i = 0; i < divs.length; i++) {
        if(i === buttonId) {
            divs[i].style.display = 'block'
        } else {
            divs[i].style.display = 'none'
        }
    }    

}

function typeEvents() {

    let buttonTask = getButtonTask()
    let buttonAdvice = getButtonAdvice()
    let buttonAppoitment = getButtonAppoitment()

    buttonTask.addEventListener('click', function() {
        tasks_divs = getTasksDivs()
        buttonTypeClick(buttonTask, tasks_divs)
    })
    buttonAdvice.addEventListener('click', function() {
        advices_tasks = getAdvicesDivs()
        buttonTypeClick(buttonAdvice, advices_tasks)
    })
    buttonAppoitment.addEventListener('click', function() {
        appointments_divs = getAppointmentsDivs()
        buttonTypeClick(buttonAppoitment, appointments_divs)
    })

}

function buttonTypeClick(button, objects) {

    if(button.className === 'button-2') {
        showDivsTAA(objects)
        button.className = 'button-2-active'
    } else if(button.className === 'button-2-active') {
        hideDivsTAA(objects)
        button.className = 'button-2'
    }
}

function showDivsTAA(objects) {

    for(let i = 0; i < objects.length; i++) {
        objects[i].style.opacity = 0.85
    }
}

function hideDivsTAA(objects) {
    
    for(let i = 0; i < objects.length; i++) {
        objects[i].style.opacity = 0.4
    }
}

function TAAEvents() {
    dayTAAEvent()
    weekTAAEvent()
    monthTAAEvent()
}

function dayTAAEvent() {

    let dayTAAs = document.querySelectorAll(".day-TAA")
    for(let i = 0; i < dayTAAs.length; i++) {
        dayTAAs[i].addEventListener('click', function() {
            TAAClick(this)
        })
    }

}

function weekTAAEvent() {

    let weekTAAs = document.querySelectorAll(".week-TAA")
    for(let i = 0; i < weekTAAs.length; i++) {
        weekTAAs[i].addEventListener('click', function() {
            TAAClick(this)
        })
    }
}

function monthTAAEvent() {

    let monthTAAs = document.querySelectorAll(".month-TAA")
    for(let i = 0; i < monthTAAs.length; i++) {
        monthTAAs[i].addEventListener('click', function() {
            TAAClick(this)
        })
    }

}

function TAAClick(TAA) {
    removeCreateDiv()
    TAA = API_TAA(TAA)
}

function API_TAA(TAA_div) {

    fetch(`TAA/${TAA_div.dataset.type}/${TAA_div.id}`)
    .then(response => response.json())
    .then(TAA => {
        TAA_div = startCreateTAAHTML(TAA)
        buttonTAAEvents(TAA_div)
    })
    
}

function buttonTAAEvents(TAA_div) {

    active_unactive_ButtonEvent(TAA_div)
    editButtonEvent(TAA_div)
    deleteButtonEvent(TAA_div)

}

function active_unactive_ButtonEvent(TAA_div) {

    active_button = TAA_div.querySelector('#mark-as-active-button')

    if(active_button != null) {
        active_button.addEventListener('click', function(e) {
            choseActiveOrUnactive(TAA_div)
        })
    } else {
        TAA_div.querySelector('#mark-as-not-active-button').addEventListener('click', function(e) {
            choseActiveOrUnactive(TAA_div)
        })
    }
}

function editButtonEvent(TAA_div) {
    TAA_div.querySelector('#edit-button').addEventListener('click', function(e) {
        editTAA(TAA_div)
    })
}

function deleteButtonEvent(TAA_div) {
    TAA_div.querySelector('#remove-button').addEventListener('click', function(e) {
        deleteTAA(TAA_div)
    })
}

function choseActiveOrUnactive(TAA_div) {
    text_active = TAA_div.querySelector('#active')
    button_active = TAA_div.querySelector('#mark-as-not-active-button')
    if(text_active.childNodes[0].textContent === 'Active') {
        frontEndUnactive(text_active, button_active)
        backEndActiveUnactive(TAA_div, false)  
    } else {
        frontEndActive(text_active, button_active)
        backEndActiveUnactive(TAA_div, true)
    } 
}

function frontEndUnactive(text_active, button_active) {
    text_active.childNodes[0].textContent = 'Disabled'
    button_active.textContent = 'Turn active'
}

function frontEndActive(text_active, button_active) {
    text_active.childNodes[0].textContent = 'Active'
    button_active.textContent = 'Turn disabled'
}

function backEndActiveUnactive(TAA_div, active) {

    type = TAA_div.dataset.type
    id = TAA_div.dataset.id

    fetch(`/active/${type}/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            active: active
        })
    })

}

function editTAA(TAA_div) {

    left_col = getLeftCol(TAA_div)
    content_div = getTAAContent(TAA_div)
    content_text = content_div.textContent
    content_div.style.display = 'none'

    putTheTextArea(TAA_div, content_text, left_col)
    putTheButtonInTAAEdit(TAA_div, left_col)

    button_edit.addEventListener('click', function(e) {
        editTextTAA(TAA_div)
    })

}

function putTheTextArea(TAA_div, content_text, left_col) {

    if(!haveAlreadyTextArea(TAA_div)) {
        textarea = document.querySelector('textarea')
        textarea = textarea.cloneNode(true)
        textarea.rows = 3
        textarea.textContent = content_text
        left_col.append(textarea)
    } else {
        TAA_div.querySelector('textarea').style.display = 'block'
    }
}

function haveAlreadyTextArea(TAA_div) {
    return TAA_div.querySelector('textarea')
}

function putTheButtonInTAAEdit(TAA_div, left_col) {

    if(!haveAlreadyButton(TAA_div)) {
        button_edit = getButtonLink()
        button_edit.textContent = 'Finish-Edit'
        left_col.append(button_edit)
    } else {
        getLeftCol(TAA_div).querySelector('button').style.display = 'block'
    }
}

function haveAlreadyButton(TAA_div) {
    return getLeftCol(TAA_div).querySelector('button')
}

function editTextTAA(TAA_div) {
    textarea = TAA_div.querySelector('textarea')
    button_textarea = getLeftCol(TAA_div).querySelector('button')
    textarea_text = textarea.value 
    button_textarea.style.display = 'none'
    textarea.style.display = 'none'
    content_div = getTAAContent(TAA_div)
    content_div.textContent = textarea_text
    content_div.style.display = 'block'

    type = TAA_div.dataset.type
    id = TAA_div.dataset.id

    fetch(`/edit/${type}/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            text: textarea_text
        })
    })
}

function deleteTAA(TAA_div) {
    
    type = TAA_div.dataset.type
    id = TAA_div.dataset.id

    if(confirm('Are you want delete?')) {
        fetch(`/delete/${type}/${id}`, {
            method: 'PUT',
        })
    
        window.location.reload()
    } 
    
}


function startCreateTAAHTML(TAA) {
    let TAA_HTML_object = createTAAHMTL(TAA)
    TAA_HTML_object.style.display = 'block'
    let TAA_div = document.querySelector("#TAA-div")
    window.scrollTo(0, 200)

    let TAA_exist = document.querySelector("#TAAElement")
    if(TAA_exist) {
        TAA_exist.remove()
    }   
    TAA_HTML_object.dataset.type = TAA.type
    TAA_HTML_object.dataset.id = TAA.TAA_id
    TAA_div.append(TAA_HTML_object)
    return TAA_HTML_object

}

function createTAAHMTL(TAA) {
    let TAA_HTML = document.createElement('div')
    TAA_HTML.className = 'div-TAA-create'
    TAA_HTML.id = 'TAAElement'
    let black_step = create_black_step(TAA)
    let white_step = create_white_step(TAA)
    TAA_HTML.append(black_step)
    TAA_HTML.append(white_step)
    return TAA_HTML
}

function create_black_step(TAA) {
    let black_step = create_black_step_div()
    let date_time = create_date_time_p(TAA)
    let days_week_div = create_days_week_div(TAA)    
    black_step.append(date_time)
    black_step.append(days_week_div)
    return black_step
}

function create_black_step_div() {
    let black_step = document.createElement('div')
    black_step.className = 'black-step'
    return black_step
}

function create_date_time_p(TAA) {
    let date_time = document.createElement('p')
    date_time.className = 'date-and-time-element'
    date_time.textContent = TAA.date_finish
    return date_time
}

function create_days_week_div(TAA) {
    let days_week_div = document.createElement('div')
    days_week_div.className = 'days-week-div'

    let days = getDays()
    
    for(let i = 0; i <= 6; i++) {
        let day = document.createElement('p')
        day.className = 'day-week'
        day.textContent = days[i][1]
        if (isAActiveDay(i, TAA.day_week)) {
            day.id = 'active-day'
        }
        days_week_div.append(day)
    }

    return days_week_div
}

function isAActiveDay(day, days) {
    
    for(let i = 0; i < days.length; i++) {
        if(day === days[i]) {
            return true
        } 
    } return false
}

function getDays() {
    let days = {
        0 : ['monday', 'M'],
        1 : ['tuesday', 'T'],
        2 : ['wednesday', 'W'],
        3 : ['thursday', 'T'],
        4 : ['friday', 'F'],
        5 : ['saturday', 'S'],
        6 : ['sunday', 'S'],
    }
    return days
}

function create_white_step(TAA) {
    let white_step = create_white_step_div()
    let left_col = create_left_col(TAA)
    let right_col = create_right_col(TAA)

    white_step.append(left_col)
    white_step.append(right_col)
    
    return white_step
}

function create_white_step_div() {
    let whitebar = document.createElement('div')
    whitebar.className = 'white-step'
    return whitebar
}

function create_left_col(TAA) {
    let left_col = create_left_col_div()
    let priority = create_priority(TAA)
    let content_element = create_content_element(TAA)
    left_col.append(priority)
    left_col.append(content_element)

    return left_col
}

function create_right_col(TAA) {
    let right_col = create_right_col_div()
    let date_created = create_date_created(TAA)
    let active = create_active(TAA)
    let is_routine = create_is_routine(TAA)
    let edit_TAA = create_edit_TAA()
    let remove_TAA = create_remove_TAA()

    right_col.append(date_created)
    right_col.append(is_routine)
    right_col.append(active)
    right_col.append(edit_TAA)
    right_col.append(remove_TAA)

    return right_col
}

function create_left_col_div() {
    let left_col = document.createElement('div')
    left_col.className = 'col'
    left_col.id = 'left-col'
    return left_col
}

function create_right_col_div() {
    let right_col = document.createElement('div')
    right_col.className = 'col'
    right_col.id = 'right-col'
    return right_col
}

function create_priority(TAA) {
    let priority = create_priority_div()
    let element_type = create_element_type(TAA)
    let element_priority = create_element_priority(TAA)
    priority.append(element_type)
    priority.append(element_priority)
    return priority
}

function create_content_element(TAA) {
    let content_element = create_content_element_div()
    let content_element_text = create_content_element_text(TAA)
    content_element.append(content_element_text)
    return content_element
}

function create_priority_div() {
    let priority = document.createElement('div')
    priority.className = 'type-priority'
    return priority
}

function create_element_type(TAA) {
    let element_type = document.createElement('p')
    element_type.className = 'element-text'
    element_type.textContent = TAA.type
    return element_type
}

function create_element_priority(TAA) {
    let element_priority = document.createElement('p')
    element_priority = checkPriority(TAA.priority, element_priority)
    return element_priority
}

function checkPriority(priority, element_priority) {
    if (priority == 4) {
        element_priority.id = 'veryhigh'
        element_priority.textContent = 'Very High'
    } else if (priority == 3) {
        element_priority.id = 'high'
        element_priority.textContent = 'High'
    } else if (priority == 2) {
        element_priority.id = 'medium'
        element_priority.textContent = 'Medium'
    } else {
        element_priority.id = 'low'
        element_priority.textContent = 'Low'
    } 

    return element_priority
}

function create_content_element_div() {
    let content_element_div = document.createElement('div')
    content_element_div.className = 'content-element'
    return content_element_div
}

function create_content_element_text(TAA) {
    let content_element_text = document.createElement('p')
    content_element_text.className = 'content-p-TAA'
    content_element_text.textContent = TAA.content
    return content_element_text
}

function create_date_created(TAA) {
    let date_created = document.createElement('div')
    date_created.className = 'date-created'
    date_created.textContent = 'Date created: ' + TAA.date_created
    return date_created
}

function create_active(TAA) {
    let active = document.createElement('div')
    let active_element = checkActive(TAA)
    active.append(active_element)
    return active
}

function create_is_routine(TAA) {
    let is_routine = document.createElement('div')
    is_routine.className = 'is-routine'
    is_routine = checkIsRoutine(is_routine, TAA)
    return is_routine
}

function create_edit_TAA() {
    let edit_TAA = getButtonLink()
    edit_TAA.textContent = 'Edit'
    edit_TAA.id = 'edit-button'
    return edit_TAA
}

function create_remove_TAA() {
    let remove_TAA = document.createElement('button')
    remove_TAA.type = 'button'
    remove_TAA.className = 'btn btn-outline-danger btn-sm'
    remove_TAA.textContent = 'Delete'
    remove_TAA.id = 'remove-button'
    return remove_TAA
}

function checkIsRoutine(is_routine, TAA) {
    if (TAA.is_routine) {
        is_routine.textContent = 'Is part of your weekly routine'
        is_routine.id = 'is-routine-true'
    } else {
        is_routine.textContent = 'Is not part of your weekly routine'
        is_routine.id = 'is-routine-false'
    } return is_routine
}

function checkActive(TAA) {
    if(TAA.active) {
        return createMarkAsNotActive()
    } else {
        return createMarkAsActive()
    }
}

function createMarkAsActive() {
    let active = document.createElement('p')
    active.className = 'is-routine'
    active.id = 'active'
    active.textContent = 'Disabled'
    let mark_as_active = getButtonLink()
    mark_as_active.id = 'mark-as-not-active-button'
    mark_as_active.textContent = 'Turn active'
    active.append(mark_as_active)
    return active
}

function createMarkAsNotActive() {
    let active = document.createElement('p')
    active.className = 'is-routine'
    active.id = 'active'
    active.textContent = 'Active'
    let mark_as_not_active = getButtonLink()
    mark_as_not_active.id = 'mark-as-not-active-button'
    mark_as_not_active.textContent = 'Turn disabled'
    active.append(mark_as_not_active)
    return active
}

function getButtonLink() {
    let button = document.createElement('button')
    button.type = 'button'
    button.className = 'btn btn-link'
    return button
}

function getAdvicesDivs() {
    divs = document.querySelectorAll("[data-type='Advice']")
    return divs
}

function getTasksDivs() {
    divs = document.querySelectorAll("[data-type='Task']")
    return divs
}

function getAppointmentsDivs() {
    divs = document.querySelectorAll("[data-type='Appointment']")
    return divs
}

function removeCreateDiv() {
    let create_div = getCreateDiv()
    create_div.style.display = "none"
}

function getCreateDiv() {
    return document.querySelector("#create-object-div")
}

function getButtonDay() {
    return document.querySelector("#day-button")
}

function getButtonWeek() {
    return document.querySelector("#week-button")
}

function getButtonMonth() {
    return document.querySelector("#month-button")
}

function getButtonTask() {
    return document.querySelector("#task-button")
}

function getButtonAdvice() {
    return document.querySelector("#advice-button")
}

function getButtonAppoitment() {
    return document.querySelector("#appoitment-button")
}

function getLeftCol(TAA_div) {
    return TAA_div.querySelector('#left-col')
}

function getRightCol(TAA_div) {
    return TAA_div.querySelector('#right-col')
}

function getTAAContent(TAA_div) {
    return TAA_div.querySelector('.content-element')
}

