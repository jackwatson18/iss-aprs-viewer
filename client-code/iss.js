
var packetTable = document.querySelector("#packet-table");

function loadAPRSpacketsFromServer() {
    fetch("https://api.kk7ewj.net/packets").then(function(response) {
        response.json().then(function(data) {
            packets = data;

            packets.forEach(function(packet) {
                var newRow = packetTable.insertRow(1);
                var newcell_1 = newRow.insertCell(0);
                var newcell_2 = newRow.insertCell(1);
                newcell_1.innerHTML = parseDateTime(packet.sent_time);
                newcell_2.innerHTML = packet.raw_packet;
            })
        })
    })
}

function parseDateTime(raw_time) {
    var time_array = raw_time.split("T");
    var time_split = time_array[1].split(".")
    var parsed_time = "D: " + time_array[0] + "\n" + "T: " + time_split[0];
    return parsed_time
}

loadAPRSpacketsFromServer();
