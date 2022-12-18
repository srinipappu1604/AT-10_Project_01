class Orange_Login:
    username = "Admin"
    password = "admin123"
    
class Orange_invalid_login:
    username = "Admin"
    password = "Invalid password"
    
class Add_New_Employee:
            firstname = "Srinivasa"
            middlename = "Prabu"
            lastname = "R"
            nickname = "Pappu"
            otherid = "Aadhar"
            driverslicencenumber = "5465h64h4ff54f5"
            licenseexpirydate = "2052-12-13"
            ssnnumber = "627826842"
            sinnumber = "365487822"
            dateofbirth = "1993-04-16"
            militaryservice = "No"
class edit_emp:
    employeeid = "4555"
    
class Orange_Selectors:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    pim_module_click ='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    pim_add_click = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    first_name = 'firstName'
    middle_name = 'middleName'
    last_name = 'lastName'
    first_save = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    nick_name = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    drivers_license_number = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    license_expiry_date = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    ssn_number = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    sin_number = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    nationality_dropdown = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    marital_status = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
    date_of_birth =  '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    gender_male = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    military_service = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    final_save = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    
    pim_select_edit = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[1]/div/div/label/span/i'
    pim_edit_existing_user = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i'
    employee_id = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input'
    edit_save = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button'
    
    pim_select_delete_employee = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/label/span/i'
    pim_delete_selected_user = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button'
    pim_delete_are_you_sure = '/html/body/div/div[3]/div/div/div/div[3]/button[2]'
    