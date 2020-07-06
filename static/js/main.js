
$('#add-comment').on('click', () => {
    var uuid = $.trim($("#article-uuid").text());
    var commentText = $('#comment-data').val();
    var date = new Date();
    if (uuid && commentText) {

        $.post(`/article/${uuid}/comment`, {data: commentText, 
            csrfmiddlewaretoken: "{{ csrf_token }}"
        });
        
        $('#comment-section').prepend(`<div class="row">
        <div class="col-md-6">
            <div><strong>Unknown Reader</strong> said: ${commentText}</div>
            <div><strong>Date Posted: </strong> ${date}</div>
            <hr/>
        </div>
    </div>`);
    }
})


function shuffle(arr) {
    var currentInt = arr.length;

    while (currentIndex !== 0) {
        // get a random int within bound of the array size
        randomInt = Math.floor(Math.random() * currentInt);
        currentInt -= 1;
        // swap the values for the shuffle
        tempval = arr[currentIndex];
        arr[currentInt] = arr[randomInt];
        arr[randomInt] = tempval;
    }

    return arr;
}
$('#shuffle').on('click', () => {
    $('#tickers').html(shuffle($('.ticker-row')))
})
