var operations = {};
operations.send = 'SEND';
operations.response = 'RESPONSE';
var isConnected = false;
/**
 * Creates a notification
 */
function create_notification(title, message, type, delay) {
    $.notify({
        // options
        title: '<strong>' + title + '</strong>',
        message: '<p>' + message + '</p>'
    },{
        // settings
        type: type,
        placement: {
            from: "top",
            align: "right"
        },
        animate: {
            enter: 'animated fadeInRight',
            exit: 'animated fadeOutRight'
        },
        delay: delay,
        template: '<div data-notify="container" class="col-xs-11 col-sm-4 alert alert-{0}" role="alert">' +
            '<button aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
            '<span data-notify="icon"></span> ' +
            '<span data-notify="title">{1}</span> ' +
            '<span data-notify="message">{2}</span>' +
            '<div class="progress" data-notify="progressbar">' +
                '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
            '</div>' +
            '<a href="{3}" target="{4}" data-notify="url"></a>' +
	    '</div>'
    });
}

function get_capabilities() {
    $('#server_ip').rules('add','required');
    $('#server_port').rules('add','required');
    $('#server_username').rules('add','required');
    $('#server_password').rules('add','required');
    if($('#tool_form').valid()){
        Sijax.request('get_capabilities', [Sijax.getFormValues('#tool_form')]);
        setProgressBar(operations.send)
        $('#btn_get_capabilities').html('Connecting..');
        $('#btn_get_capabilities').prop("disabled", true );
    }
    $('#server_ip').rules('remove','required');
    $('#server_port').rules('remove','required');
    $('#server_username').rules('remove','required');
    $('#server_password').rules('remove','required');
}

function connected(){
    $('#server_ip').prop( "readonly", true );
    $('#server_port').prop( "readonly", true );
    $('#server_username').prop( "readonly", true );
    $('#server_password').prop( "readonly", true );
    $('#btn_get_capabilities').html('Disconnect');
    $('#btn_get_capabilities').attr('onclick','disconnect();');
    $('#btn_get_capabilities').prop("disabled", false);
    $('#div_connection').removeClass('panel-default');
    $('#div_connection').addClass('panel-success');
    $('#div_connection_header').text('Connected');
    $('#div_connection_header').css('color', '#ffffff');
    $('#lnk_show_capabilities').fadeIn()
    $('#div_connection_header').click();
    isConnected = true
    setProgressBar(operations.response)
    $('#div_capabilities_table').html('')
}

function add_capability(capability){
    $('#div_capabilities_table').append( "<tr><td>" + capability + "</td></tr>" );
}

function disconnect(){
    $('#server_ip').prop( "readonly", false );
    $('#server_port').prop( "readonly", false );
    $('#server_username').prop( "readonly", false );
    $('#server_password').prop( "readonly", false );
    $('#server_password').attr( "value", '' );
    $('#btn_get_capabilities').html('Connect');
    $('#btn_get_capabilities').attr('onclick','get_capabilities();');
    $('#div_connection').removeClass('panel-success');
    $('#div_connection').addClass('panel-default');
    $('#div_connection_header').text('Not connected');
    $('#div_connection_header').css('color', '#2c3e50');
    $('#lnk_show_capabilities').fadeOut()
    isConnected = false
}

function send_command(){
    if(isConnected){
        $('#xml_command').rules('add','required');
        if($('#tool_form').valid()){
            Sijax.request('send_command', [Sijax.getFormValues('#tool_form')]);
            setProgressBar(operations.send)
        }
        $('#xml_command').rules('remove','required');
        $('#xml_response').text('');
    }
    else {
        create_notification('Not connected','Please connect to a NETCONF server before sending requests','danger',0);
        $('#server_ip').focus();
    }
}

function show_xml_response(base64_string){
    var xml = atob(base64_string);
    var format_xml = formatXml(xml);
    $('#xml_response').text(format_xml);
    // Add style to response
    $('pre code').each(function(i, block) {
        hljs.highlightBlock(block);
    });
    setProgressBar(operations.response)
}

function setProgressBar(operation){
    if (operation == operations.send){
        $('#div_progress').css('width','50%');
    }
    else if (operation == operations.response){
        $('#div_progress').css('width','100%');
        setTimeout(function(){$('#div_progress').css('width','0%')}, 2000);
    }
}

function generate_code(){
    xml_command = document.getElementById("xml_command").value
    code_template = $('#div_code_template').text()
    code_generated = code_template.replace('xml = """"""', 'xml = """' + xml_command + '"""')
    $('#generated_code').text(code_generated)
}

function formatXml(xml) {
    var formatted = '';
    var reg = /(>)(<)(\/*)/g;
    xml = xml.replace(reg, '$1\r\n$2$3');
    var pad = 0;
    jQuery.each(xml.split('\r\n'), function(index, node) {
        var indent = 0;
        if (node.match( /.+<\/\w[^>]*>$/ )) {
            indent = 0;
        } else if (node.match( /^<\/\w/ )) {
            if (pad != 0) {
                pad -= 1;
            }
        } else if (node.match( /^<\w[^>]*[^\/]>.*$/ )) {
            indent = 1;
        } else {
            indent = 0;
        }

        var padding = '';
        for (var i = 0; i < pad; i++) {
            padding += '  ';
        }

        formatted += padding + node + '\r\n';
        pad += indent;
    });

    return formatted;
}

