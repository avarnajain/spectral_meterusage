"use strict";

function updateGraph(data) {
    // console.log('inside update graph')
    if (data.successful) {
        const image_path = data.successful
        // console.log('image_path on js', image_path)
        $('#graph').html(`<h1>Meter Usage Data</h1><img id="theImg" src="../static/${image_path}"/>`);
    }
    else {
        const error_message = data.error
        // console.log('inside error condition')
        $('#graph').html(`<p>${error_message}</p>`);
    }
}

function getData(evt) {
    // console.log('inside jquery function')
    evt.preventDefault();
    evt.stopImmediatePropagation()
    let formInputs = {
        // console.log('inside formInputs')
        "start_date": $('#start_date_id').val(),
        "end_date": $('#end_date_id').val()
    };
    // console.log('after formInputs')
    $.post("/get-data", formInputs, updateGraph);
    // console.log('after post')
}

$("#dates").on('submit', getData);


