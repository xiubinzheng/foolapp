
$('#add-comment').on('click', () => {
    var uuid = $.trim($("#article-uuid").text());
    var commentText = $('#comment-data').val();
    var now = new Date();
    
    now.setHours(now.getHours());
    var isPM = now.getHours() >= 12;
    var isMidday = now.getHours() == 12;
    var time =now.getMonth() +' ' +now.getDate()+' '+ [now.getHours() - (isPM && !isMidday ? 12 : 0), 
                now.getMinutes() ].join(':') +
            (isPM ? ' p.m.' : ' a.m.');
    if (uuid && commentText) {

        $.post(`/article/${uuid}/comment`, {data: commentText, 
            csrfmiddlewaretoken: "{{ csrf_token }}"
        });
        
        $('#comment-section').prepend(`<div class="row">
        <div class="col-md-6">
            <div><strong>Unknown Reader</strong> said: ${commentText}</div>
            <div><strong>Date Posted: </strong> ${time}</div>
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
