function convert() {
    if(document.KBtoMB.KB.value) {
        document.KBtoMB.MB.value = eval(document.KBtoMB.KB.value / 1024);
    }
    else {
        if(document.KBtoMB.MB.value) {
            document.KBtoMB.KB.value = eval(document.KBtoMB.MB.value * 1024);
        }
    }
}