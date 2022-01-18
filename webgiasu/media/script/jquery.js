//report post
$(".report-btn").click(function(e){
    let post_id = e.target.id
    console.log(post_id)
    $.ajax({
        url: '{% url "reportpost" %}',
        type: 'POST',
        data:{id:post_id,}
    })
    .done(function(response){
        if (response['success'] == false){
            if (response['detail'] == "0"){
                console.log("Cant take info of contact in server process.")
                $("#notifModalLabel").html("Lỗi truy vấn server")
                $('#notificationmodal').modal('show')
                
            }
            else if (response['detail'] == "1"){
                console.log("Need to logged to do this action.")
                $("#notifModalLabel").html("Bạn cần phải đăng nhập")
                $('#notificationmodal').modal('show')
                $("#modal-footer-notif-login-button").show()
            }
        }
        else if (response['success'] == true){
            if (response['detail'] == 'like')
            {
                let num_reports_display_id = "#num_reports_display" + post_id
                $(num_reports_display_id).html(response['num'] + " reports")
            }
            else if (response['detail'] == 'unlike')
            {
                let num_reports_display_id = "#num_reports_display" + post_id
                $(num_reports_display_id).html(response['num'] + " reports")
            }
        }
    })
    .fail(function(response){
        alert("Lỗi request")
    })
})
//display image
$(".img-click-display").click(function(e){
    var link = e.target.id
    $("#displayimageBody").attr('src', link)
})
//Get user info
$(".link-display-user-info").click(function(e){
    console.log(e.target.id)
    var user_id = e.target.id
    $.ajax({
        url: '{% url "showinfo" %}',
        type: 'POST',
        data:{id:user_id,}
    })
    .done(function(response){
        if (response['success'] == 'False'){
            if (response['detail'] == "0"){
                console.log("Cant take info of contact in server process.")
                $("#infoModalLabel").html("Không tìm thấy thông tin yêu cầu")
            }
            else{
                console.log("Need to logged to do this action.")
                $("#infoModalLabel").html("Bạn cần phải đăng nhập.")
                $("#modal-footer-info-login-button").show()
            }
        }
        else{
            $("#modal-footer-info-login-button").hide()

            $("#infoModalLabel").html("Thông tin " + response['full_name'])

            $("#school").html("Trường: " + response['school'])
            $("#specialize").html("Chuyên môn: " + response['specialize'])
            $("#yearofschool").html("Năm học: " + response['yearofschool'])
            $("#sexs").html("Giới tính: " + response['sexs'])
            $("#years_of_birth").html("Ngày sinh: " + response['years_of_birth'])
            $("#more").html("Mô tả thêm: " + response['more'])

            let date = response['last_login']
            let nt_date = date[11] + date[12] + date[13] + date[14] + date[15] + date[16] + date[17] + date[18] + ", " + date[8] + date[9] + "/" + date[5] + date[6] + "/" + date[0] + date[1] + date[2] + date[3]

            $("#last_login").html("Lần đăng nhập cuối: " + nt_date )

            if (response['school'] == null || response['school'] == '')
            {
                $("#iconschool").css("color", "#cc0000")
            }
            else{
                $("#iconschool").css("color", "#10B33C")
            }
            
            if (response['specialize'] == null || response['specialize'] == '')
            {
                $("#iconspecialize").css("color", "#cc0000")
            }
            else{
                $("#iconspecialize").css("color", "#10B33C")
            }

            if (response['yearofschool'] == null || response['yearofschool'] == '')
            {
                $("#iconyearofschool").css("color", "#cc0000")
            }
            else{
                $("#iconyearofschool").css("color", "#10B33C")
            }

            if (response['sexs'] == null || response['sexs'] == '')
            {
                $("#iconsexs").css("color", "#cc0000")
            }
            else{
                $("#iconsexs").css("color", "#10B33C")
            }

            if (response['years_of_birth'] == null || response['years_of_birth'] == '')
            {
                $("#iconyears_of_birth").css("color", "#cc0000")
            }
            else{
                $("#iconyears_of_birth").css("color", "#10B33C")
            }

            if (response['more'] == null || response['more'] == '')
            {
                $("#iconmore").css("color", "#cc0000")
            }
            else{
                $("#iconmore").css("color", "#10B33C")
            }

            
        }
    })
    .fail(function(response){
        console.log("FAIL")
    })
})
//Get contact
$(".butoncontact").click(function(e){
    console.log(e.target.id)
    post_id = e.target.id
    $.ajax({
        url: '{% url "getcontact" %}',
        type: 'POST',
        data:{id:post_id,}
    })
    .done(function(response){
        if (response['success'] == 'False'){
            if (response['detail'] == "0"){
                console.log("Cant take info of contact in server process.")
                $("#notifModalLabel").html("Không tìm thấy thông tin yêu cầu")
                $('#notificationmodal').modal('show')
                
            }
            else{
                console.log("Need to logged to do this action.")
                $("#notifModalLabel").html("Bạn cần phải đăng nhập")
                $('#notificationmodal').modal('show')
                $("#modal-footer-notif-login-button").show()
            }
        }
        else{
            console.log(response['contact'])

            $("#contactlable" + post_id).html(response['contact'])
            $("#modal-footer-notif-login-button").hide()
        }
    })
    .fail(function(response){
        console.log("FAIL")
    })
})
//Upload post
$(".btn-post-findtutor").click(function(){
    let title = $("#titleid").val()
    let main_content = $("#main_contentid").val()
    let subject = $("#subjectid").val()
    let calendar = $("#calendarid").val()
    let salary = $("#salaryid").val()
    let contact = $("#contactid").val()
    let date_outdate = $("#date_outdateid").val()
    let post_img1 = $("#post_img1id").val()
    let post_img2 = $("#post_img2id").val()
    let post_img3 = $("#post_img3id").val()

    var f_obj1 = $("#post_img1id")[0].files[0]
    var f_obj2 = $("#post_img2id")[0].files[0]
    var f_obj3 = $("#post_img3id")[0].files[0]
    var data = new FormData()
    data.append("img1",f_obj1)   
    data.append("img2",f_obj2)   
    data.append("img3",f_obj3)   

    var valid = true

    if (title == ''){
        alert('Tiêu đề không được trống.')
        valid = false
    }
    if (main_content == ''){
        alert('Nội dung không được trống.')
        valid = false
    }
    if (subject == ''){
        alert('Môn học không được trống.')
        valid = false
    }
    if (calendar == ''){
        alert('Lịch học không được trống.')
        valid = false
    }
    if (salary == ''){
        alert('Chi trả dự tính không được trống.')
        valid = false
    }
    if (contact == ''){
        alert('Thông tin liên hệ không được trống.')
        valid = false
    }
    if (contact == ''){
        alert('Thông tin liên hệ không được trống.')
        valid = false
    }
    if (date_outdate == ''){
        alert('Ngày hết hạn không được trống.')
        valid = false
    }

    if (post_img1){
        if ($('#post_img1id')[0].files[0].size > 3072000){
            alert('File 1 quá lớn')
            valid = false
        }
    }
    if (post_img2){
        if ($('#post_img2id')[0].files[0].size > 3072000){
            alert('File 2 quá lớn')
            valid = false
        }
    }
    if (post_img3){
        if ($('#post_img3id')[0].files[0].size > 3072000){
            alert('File 3 quá lớn')
            valid = false
        }
    }
    

    if (valid == true)
    {
        data.append('title',title)
        data.append('main_content',main_content)
        data.append('subject',subject)
        data.append('calendar',calendar)
        data.append('salary',salary)
        data.append('contact',contact)
        data.append('date_outdate',date_outdate)
        $.ajax({
            url: '{% url "getpostpost" %}',
            type: 'POST',
            processData:false,
            contentType:false,
            data:data
        })
        .done(function(response){
            if (response['success'] == false){
                alert(response['detail'])
            }
            else{
                console.log("SAVED")
                location.reload()
            }
        })
        .fail(function(response){
            alert('Lỗi truyền tải')
        })
    }
})