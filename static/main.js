// This function initializes all the interactive elements on the webpage.
$(document).ready(function() {

    // Initializes tooltips for elements that have the data-toggle attribute set to "tooltip".
    initializeTooltips();

    // Animates buttons by enlarging them when they are hovered over.
    animateButtonsOnHover();

    // Shows a modal with comprehensive details about the documentation when a button is clicked.
    handleButtonClick();
});

/**
 * Initializes tooltips for better user guidance.
 */
function initializeTooltips() {
    $('[data-toggle="tooltip"]').tooltip();
}

/**
 * Adds an enlarging animation to buttons on hover for a more interactive feel.
 */
function animateButtonsOnHover() {
    $('.btn').hover(function() {
        enlargeElement($(this), '1.1em');
    }, function() {
        shrinkElement($(this), '1em');
    });
}

/**
 * Enlarges a DOM element to a specified size.
 * @param {Object} element - The jQuery object of the DOM element.
 * @param {string} size - The size to enlarge to.
 */
function enlargeElement(element, size) {
    element.animate({ fontSize: size }, 200);
}

/**
 * Shrinks a DOM element to a specified size.
 * @param {Object} element - The jQuery object of the DOM element.
 * @param {string} size - The size to shrink to.
 */
function shrinkElement(element, size) {
    element.animate({ fontSize: size }, 200);
}

/**
 * Displays a modal when a documentation button is clicked, guiding the user about its functionality.
 */
function handleButtonClick() {
    $('.btn').click(function(e) {
        e.preventDefault();
        const documentationType = $(this).text().trim();
        displayDocumentationModal(documentationType);
    });
}

/**
 * Displays a modal with information about the chosen documentation type.
 * @param {string} docType - The type of documentation (e.g., "ReDoc" or "FastAPI Docs").
 */
function displayDocumentationModal(docType) {
    const docInfo = {
        "ReDoc": {
            description: "ReDoc provides a responsive web interface for viewing and testing your API endpoints.",
            link: "/redoc"
        },
        "FastAPI Docs": {
            description: "FastAPI Docs provides an interactive interface to test your API endpoints directly.",
            link: "/docs"
        }
    };

    let modal = constructModal(docType, docInfo[docType].description, docInfo[docType].link);
    $('body').append(modal);
    $('#infoModal').modal('show');

    // Cleanup the modal after use to prevent duplicate modals in the DOM.
    $('#infoModal').on('hidden.bs.modal', function() {
        $(this).remove();
    });
}

/**
 * Constructs a modal with the provided information.
 * @param {string} title - The modal's title.
 * @param {string} content - The main content of the modal.
 * @param {string} link - The link the modal's button should point to.
 * @returns {string} - The constructed modal as an HTML string.
 */
function constructModal(title, content, link) {
    return `
        <div class="modal fade" id="infoModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">${title} Information</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">${content}</div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        <a href="${link}" class="btn btn-primary">Go to ${title}</a>
                    </div>
                </div>
            </div>
        </div>
    `;
}
