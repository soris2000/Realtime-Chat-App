import flet as ft

# SignUp Form
class SignUpForm(ft.UserControl):
    def __init__(self, submit_values,btn_signin):
        super().__init__()
        #Return values user and password
        self.submit_values = submit_values
        #Route to signup Form
        self.btn_signin = btn_signin
        

    def btn_signup(self, e):
        if not self.text_user.value:  
            self.text_user.error_text="Name cannot be blank!"
            self.text_user.update()
        if not self.text_password.value:
            self.text_password.error_text="Password cannot be blank!"
            self.text_password.update()
        else:
            #Return values 'user' and 'password' as arguments 
            self.submit_values(self.text_user.value,self.text_password.value)
    def build(self):
        self.title_form=ft.Text(value="Create your account",text_align=ft.TextAlign.CENTER,size=30, )
        self.text_user = ft.TextField(label="User Name")
        self.text_password = ft.TextField(
            label="Password", password=True, can_reveal_password=True
        )
        self.text_signup=ft.ElevatedButton(text="Sign up",color=ft.colors.WHITE,width=150,height=50,on_click= self.btn_signup)
        self.text_signin=ft.Row(controls=[ft.Text(value="Already have an account?"),ft.TextButton(text="Sign in",on_click=self.btn_signin)],alignment=ft.MainAxisAlignment.CENTER)
        

        return ft.Container(
            width=500,
            height=560,
            bgcolor=ft.colors.TEAL_800,
            padding=30,
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Column(
                [
                    self.title_form,
                    ft.Container(height=30),
                    self.text_user,
                    self.text_password,
                    ft.Container(height=10),
                    self.text_signup,
                    ft.Container(height=20),
                    self.text_signin,
                    
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
       
