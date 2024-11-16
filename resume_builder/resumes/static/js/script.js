// JavaScript to handle the addition of new fields
function addField(section) {
    const container = document.getElementById(`${section}-container`)
    const input = document.createElement('input')
    input.type = 'text'
    input.name = `${section}[]`
    input.className = section.slice(0, -1) // remove the trailing 's'
    container.insertBefore(input, container.querySelector('.add-btn'))
}

// JavaScript to show/hide experience details based on the dropdown selection
document.getElementById('experience').addEventListener('change', function () {
    const value = this.value
    const details = document.getElementById('experience-details')
    if (value === 'fresher') {
        details.style.display = 'none'
        document.getElementById('recent-company').value = ''
        document.getElementById('recent-duration').value = ''
    } else {
        details.style.display = 'flex'
    }
})

