function onStart()
{
    $.ajax({
        type: "PUT",
        url: "/start",
        success: res => {
            console.log("Start erfolgreich!");
            handleAction(true);
        },
    });
}

function onStop()
{
    $.ajax({
        type: "PUT",
        url: "/stop",
        success: res => {
            console.log("Stop erfolgreich!");
            handleAction(false)
        },
    });
}

function getRecordingData()
{
    let selectedDate = document.getElementById("inInfo").value;
    const date = new Date(selectedDate);
    const formattedDate = `${date.getDate()}.${(date.getMonth() + 1).toString().padStart(2, "0")}.${date.getFullYear()}`;

    $('#pSelectedDate').text(formattedDate);

    $.ajax({
        type: "GET",
        url: `/recdata/${formattedDate}`,
        success: res => {
            console.log(res);

            $("#ulData").empty();
            var ul = $("#ulData")[0];
            res.forEach(elm => {
                let li = document.createElement("li");
                li.appendChild(document.createTextNode(elm));
                ul.appendChild(li);
            });
        },
    });
}

function handleAction(start)
{
    if(start)
    {
        $("#divStart").css("border", "1px solid grey");
        $("#divStart").css("background", "grey");
        $("#divStart").css("pointer-events", "none");

        $("#divTriangle").css("border-color", "transparent transparent transparent white");

        $("#divStop").css("background", "red");
        $("#divStop").css("border", "1px solid red");
        $("#divStop").css("pointer-events", "auto");
    }
    else
    {
        $("#divStart").css("border", "1px solid #01DF01");
        $("#divStart").css("background", "white");
        $("#divStart").css("pointer-events", "auto");

        $("#divTriangle").css("border-color", "transparent transparent transparent #01DF01");

        $("#divStop").css("background", "grey");
        $("#divStop").css("border", "1px solid grey");
        $("#divStop").css("pointer-events", "none");
    }
}