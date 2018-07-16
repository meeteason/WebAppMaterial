const repoPath = 'ipfs-' + Math.random()
const node = new Ipfs({
    init: false,
    start: false,
    repo: repoPath
})
node.init(handleInit)
function handleInit(err) {
    if (err) {
        throw err
    }
    node.start(() => {
        console.log('Online status: ', node.isOnline() ? 'online' : 'offline')
    })
}
// \u52a0\u8f7d\u6587\u4ef6
document.querySelector('#getfileinput').addEventListener('change', function () {
    var that = this, filereader;
    var upFileName = that.files[0].name;
    var index1 = upFileName.lastIndexOf(".");
    var index2 = upFileName.length;
    var upFileSuffix = upFileName.substring(index1 + 1, index2);
    if (that.files.length > 0) {
        filereader = new FileReader();
        filereader.onload = function (e) {
            if (node.isOnline()) {
                node.files.add(new node.types.Buffer(this.result), (err, res) => {
                    if (err || !res) {
                        return console.error('Error - ipfs files add', err, res)
                    }
                    res.forEach((file) => upload_result(file.hash, upFileSuffix))
                })
            } else {
                alert('\u8fd8\u6ca1\u51c6\u5907\u597d,\u8bf7\u7a0d\u5019\u518d\u8bd5');
            }
        };
        filereader.readAsArrayBuffer(that.files[0]);
    }
}, false);

function upload_result(fileHash, fileSuffix) {
    var server = Math.floor(Math.random() * 5);
    var picurl = 'http://p' + server + '.cdn.img9.top/ipfs/' + fileHash + '?' + server + '.' + fileSuffix;
    $('#up_result').append(picurl + "\n");
    if (fileSuffix == 'jpg' || fileSuffix == 'jpeg' || fileSuffix == 'png' || fileSuffix == 'gif') {
        getimg(picurl);
    }
}

function getimg(picurl) {
    var thediv = $('<div class="col-md-2"></div>');
    var thelink = $('<a target="_blank"></a>');
    var img = new Image();
    img.src = picurl;
    img.className = 'img-thumbnail';
    img.addEventListener("load", function () {
        publish(picurl);
    }, false);
    thelink.append(img);
    thediv.append(thelink);
    $('#other_img').prepend(thediv);
}

function publish(picurl) {
    $.get('/main/publish?picurl=' + picurl, function (result) {
        console.log(result);
    });
}