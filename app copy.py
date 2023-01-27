from flet import *
wallpaper = 'assets/icons/wallpaper.png'
w= 1000
h=800
sbw = 50
s_bw = 270
csw = 300
dmw = w-300-50
br = 12
s_btn_w = 40
s_btn_h = 35 
sbc = '#282828'
csc = '#202020'
dmc = '#282828'
sb_ic = '#efefef'
s_btn_h_c ='#E6353535'
ic = "#00a884"
nac = '#25d366'
chat_screen_padding = 20
ih_br = 5
htc = "#6a6a6a"
rc = "#363636"
sc = "#035d4d"
mtc = "#689e94"
smc = "#cddfdb"
class App(UserControl):
  def __init__(self,pg:Page):
    super().__init__()
    self.pg = pg
    self.containers_init()
    self.init_helper()

  def load_chat_dummy(self):
    # for n in range(5):
      # self.chats_contents_column.controls.append(self.chat_row) 
      # self.chats_contents_column.update()  
    pass  


  def init_helper(self):
    self.pg.add(
      Container(
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        border_radius=br,
        expand=True,
        bgcolor=dmc,
        content=Row(
          spacing=0,
          controls=[
            self.sidebar,
            self.chats_screen,
            self.dm_screen,
          ]
        )
      )
    )  
  
  def containers_init(self):
    self.dm_screen_content_main()
    self.chats_column_f()
    self.chat_screen()
    self.sidebar()
    self.base_containers()
    self.load_chat_dummy()
    
  def base_containers(self):
    self.sidebar = Container(
      padding=padding.only(top=50,bottom=50),
      width=sbw,
      bgcolor=sbc,
      content=self.sidebar_column,
    )
    self.chats_screen = Container(
      width=csw,
      bgcolor=csc,
      content=self.chat_screen_items,
    )
    self.dm_screen = Container(
      expand=True,
      bgcolor=dmc,
      content=self.dm_screen_content
    )

  def sidebar_btn_hovered(self,e:HoverEvent):
    if e.data == 'true':
      e.control.bgcolor = s_btn_h_c
      
    else:  
      e.control.bgcolor = None
    e.control.update()  

  def sidebar(self):
    self.sidebar_column = Column(
      horizontal_alignment='center',
      alignment='spaceBetween',
      spacing=0,
      controls=[
        Column(
          controls=[
            Container(
              # on_hover=self.sidebar_btn_hovered,
              alignment=alignment.center,
              height=s_btn_h,
              width=s_btn_w,
              bgcolor = s_btn_h_c,
              border_radius=5,
              content=Row(
                spacing=0,
                alignment='spaceBetween',
                vertical_alignment='center',
                controls=[
                  Container(
                    offset=transform.Offset(0, 0),
                    animate_offset=animation.Animation(1000),
                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                    height=17,
                    width=3,
                    bgcolor=ic,
                    border_radius=5
                  ),
                  Container(
                    margin=margin.only(right=10),
                    content= Stack(
                      controls=[
                        Container(
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          height=20,
                          width=20,
                          content=Image(
                            src='assets/icons/c.png',
                            fit=ImageFit.COVER,
                            color=sb_ic
                          )
                        ),
                        Container(
                          right=1,
                          top=1,
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          height=8,
                          width=8,
                          bgcolor=nac,
                          border_radius=20
                        ),
                      ]
                    )
                
                  )
                 ]
              )
            ),
            
            Container(
              on_hover=self.sidebar_btn_hovered,
              alignment=alignment.center,
              height=s_btn_h,
              width=s_btn_w,
              # bgcolor = s_btn_h_c,
              border_radius=ih_br,
              content=Row(
                spacing=0,
                alignment='spaceBetween',
                vertical_alignment='center',
                controls=[
                  Container(
                    offset=transform.Offset(0, 0),
                    animate_offset=animation.Animation(1000),
                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                    height=17,
                    width=3,
                    # bgcolor=ic,
                    border_radius=5
                  ),
                  Container(
                    margin=margin.only(right=10),
                    content= Stack(
                      controls=[
                        Container(
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          height=20,
                          width=20,
                          content=Image(
                            src='assets/icons/s.png',
                            fit=ImageFit.COVER,
                            color=sb_ic
                          )
                        ),
                        Container(
                          right=0,
                          top=1,
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          height=9,
                          width=9,
                          bgcolor=nac,
                          border_radius=20,
                          # border=border.all(color=sbc,width=1)
                        ),
                      ]
                    )
                
                  )
                 ]
              )
            ),

          ]

        ),


        Column(
          spacing=5,
          controls=[
            Container(
              on_hover=self.sidebar_btn_hovered,
              alignment=alignment.center,
              height=s_btn_h,
              width=s_btn_w,
              border_radius=5,
              content=Row(
                spacing=0,
                alignment='center',
                controls=[
                  Icon(
                    icons.SETTINGS_OUTLINED,
                    size=20,
                    color=sb_ic
                  )
                ]
              )
            ),


            Container(
              on_hover=self.sidebar_btn_hovered,
              alignment=alignment.center,
              height=s_btn_h,
              width=s_btn_w,
              border_radius=ih_br,
              content=Row(
                spacing=0,
                alignment='center',
                controls=[
                  Container(
                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                    height=20,
                    width=20,
                    bgcolor='red',
                    border_radius=20,
                    content=Image(
                      src='assets/dp.jpg',
                      fit=ImageFit.COVER
                    )
                  )
                ]
              )
            ),

            
          ]
        ),

      ]

    )
    
  def chat_screen(self):
    self.chat_screen_items = Stack(
      controls=[
        Column(
          controls=[
            Container(
              height=40,
              padding = padding.only(left=10),
              # margin=margin.only(bottom=10),
              content=Row(
                controls=[
                  Image(
                    src='assets/icons/logo.png',

                  ),
                  Text(
                    value='WhatsApp',
                    size=14,
                  )

                ]
              )
            ), # whatsapp icon
            
            Container(
              padding = padding.only(left=chat_screen_padding,right=chat_screen_padding),
              content=Row(
                spacing=0,
                alignment='spaceBetween',
                vertical_alignment='center',
                controls=[
                  Text(
                    value='Chats',
                    size=24,
                    weight=FontWeight.W_500
                  ),
                  Row(
                    controls=[
                      Container(
                        on_hover=self.sidebar_btn_hovered,
                        height=40,
                        width=40,
                        border_radius=ih_br,
                        content=Image(
                          src='assets/icons/newchat.png',
                          color=sb_ic
                        ),
                      ),
                      Container(
                        on_hover=self.sidebar_btn_hovered,
                        height=40,
                        width=40,
                        border_radius=ih_br,
                        content=Image(
                          src='assets/icons/more.png',
                          color=sb_ic
                        ),
                      ),
                    ]
                  )
                ]
              )
            ), # Chats label text and new chat icon and more
            
            Container(
              content=Row(
                alignment='center',
                controls=[
                  Container(
                    
                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                    border_radius = ih_br,
                    content=Container(
                      # on_hover=self.sidebar_btn_hovered,
                      clip_behavior=ClipBehavior.ANTI_ALIAS,
                      border_radius = ih_br,
                      height=35,
                      width=s_bw,
                      bgcolor=sbc,
                      border=border.only(bottom=border.BorderSide(width=1,color=htc)),
                      content=Row(
                        controls=[
                          Container(
                            width=230,
                            padding=padding.only(left=15,top=5),
                            content=TextField(
                              border=InputBorder.NONE,
                              hint_text='Search or start a new chat',
                              hint_style=TextStyle(
                                size=14,
                                font_family='arial',
                                color=htc
                              ),
                              color=sb_ic,
                              text_style=TextStyle(
                                size=14,
                                font_family='arial',
                                color=sb_ic
                              ),
                            ),
                          ),

                          Container(
                            height=25,
                            width=25,
                            border_radius=ih_br,
                            on_hover=self.sidebar_btn_hovered,
                            content=Icon(
                              icons.SEARCH_OUTLINED,
                              size=16,
                              color=htc
                            ),
                          )

                        ]
                      )
                    )
                  )
                ]

              )
            ), # search box
            
            Container(
              clip_behavior=ClipBehavior.ANTI_ALIAS,
              height=40,
              padding=padding.only(left=10,right=10),
              # border_radius=20,
              content=Container(
                border_radius=ih_br,
                on_hover=self.sidebar_btn_hovered,
                padding=padding.only(left=10,right=10),
                content=Row(
                  vertical_alignment='center',
                  alignment='spaceBetween',
                  controls=[
                    Icon(
                      icons.DELETE_OUTLINE
                    ),
                    Container(
                      content=Text(
                        value='Archived',
                        weight=FontWeight.W_600
                      ),
                      margin=margin.only(right=100)
                    ),
                    Text(
                      value='2',
                      color=ic,
                      weight=FontWeight.W_600
                    )

                  ]
                )
              )

            ), # archived chat button

            self.chats_contents_column,  
            
          ]
        ),
        Column(
          controls=[
            Container(), # whatsapp icon
            Container(), # Status text label
            Container(), # my stat
            Container(), # recent updates label
            Container(), # stats column container
          ]
        ),
      ]
    )
  
  def search_on_focus(self,e):
    pass

  def chats_column_f(self):
    self.chat_row = Container(
                  height=70,
                  padding=padding.only(left=10,right=10),
                  content=Container(
                    border_radius=ih_br,
                    on_hover=self.sidebar_btn_hovered,
                    content=Row(
                      spacing=0,
                      alignment='spaceBetween',
                      vertical_alignment='center',
                      controls=[
                        Container(
                          height=50,
                          width=50,
                          bgcolor='blue',
                          border_radius=30
                        ),
                        
                        Column(
                          alignment='center',
                          horizontal_alignment='center',
                          controls=[
                            Container(
                              width=200,
                              content=Row(
                                  alignment='spaceBetween',
                                  # vertical_alignment='center',
                                  spacing=0,
                                  controls=[
                                    Container(
                                      clip_behavior=ClipBehavior.ANTI_ALIAS,
                                      width=120,
                                      content=Text(
                                      'Some long name that will overflow',
                                      no_wrap=True
                                    ),
                                    ),
                                    Text(
                                      '12:20AM'
                                    ),
                                  ]
                                ),
                            ),
                            
                            


                            Container(
                              width=200,
                              content=Row(
                                  alignment='spaceBetween',
                                  # vertical_alignment='center',
                                  spacing=0,
                                  controls=[
                                    Container(
                                      clip_behavior=ClipBehavior.ANTI_ALIAS,
                                      width=120,
                                      content=Text(
                                      'Some long name that will overflow',
                                      no_wrap=True
                                    ),
                                    ),
                                    Text(
                                      '12:20AM'
                                    ),
                                  ]
                                ),
                            ),
                            
                            

                            

                          ]
                        )
                      ]
                    )
                  )

                )
            
    self.chats_contents_column = Column(
              scroll='auto',
              expand=True,
              controls=[
                self.chat_row,
           
              ]
            ) # chats column container

  def msg_hovered(self,e):
    if e.data == 'true':
      self.msg_hover_emoji.visible = True
    else:  
      self.msg_hover_emoji.visible = False
    self.msg_hover_emoji.update()

  def show_msg_menu(self,e:LongPressEndEvent):
    print(e.target)
      
  def dm_screen_content_main(self):


    self.msg_hover_emoji = PopupMenuButton(
        tooltip=None,
        content=Container(
          tooltip=None,
          height=20,
          width=20,
          border_radius=25,
          content=Icon(
            icons.EMOJI_EMOTIONS_OUTLINED,
            color=htc
          ),
        ),
        items=[
            PopupMenuItem(
              content=Row(
                controls=[
                  Image(
                    src='assets/icons/laugh.png',
                  ),
                  Icon(
                    icons.ABC,
                  ),
                  Icon(
                    icons.ABC,
                  ),
                ]
              )
            )
           
        ]
    # )
    )

    self.msg_container = Stack(
      # spacing=0,
      controls=[
        Container(
          margin=margin.only(right=6),
          alignment=alignment.center_left,
          width = 500,
          padding=10,
          bgcolor=sc,
          border_radius=ih_br,
          content=Column(
            spacing=4,
            controls=[
              Text(
                value="Lorem  Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                selectable=True,
                color=smc,
                weight=FontWeight.W_400,
                size=14,
                
              ),
              Row(
                spacing=4,
                alignment='end',
                controls=[
                  Text(
                    '5:30 AM',
                    size=10,
                    weight=FontWeight.W_600,
                    color=mtc
                  ),
                  Icon(
                    icons.DONE,
                    color=mtc,
                    size=10
                  )
                ]
              )
            ]
          )
        ),
        Container(
          height=20,
          width=20,
          shape=BoxShape.RECTANGLE,
          bgcolor=sc,
          right=0,
          border_radius=BorderRadius(topLeft=0, topRight=0, bottomLeft=0, bottomRight=20)

        ),
        
      ]
    )

    self.msg_obj = Container(
      on_long_press=self.show_msg_menu,
      on_hover=self.msg_hovered,
      content=Row(
        spacing=25,
        alignment='end',
        vertical_alignment='center',
        controls=[
          self.msg_hover_emoji,
          self.msg_container,
          
          
        ]
      )
    )

    self.dm_screen_content = Container(
      content=Column(
        spacing=0,
        controls=[
          Container(
            # bgcolor='red',
            content=WindowDragArea(
              content=Container(height=40)
            )

          ),
          Container(
            padding=padding.only(left=20,right=15),
            height=50,
            content=Row(
              alignment='spaceBetween',
              controls=[
                Row(
                  controls=[
                    Container(
                      height=40,
                      width=40,
                      border_radius=20,
                      bgcolor=rc,
                      content=Icon(
                        icons.PERSON
                      )
                    ),
                    Text(
                      value='#Se7en🙏'
                    )
                    
                  ]
                ),
                Row(
                  controls=[
                    Container(
                      on_hover=self.sidebar_btn_hovered,
                      alignment=alignment.center,
                      height=s_btn_h,
                      width=s_btn_w,
                      border_radius=5,
                      content=Row(
                        spacing=0,
                        alignment='center',
                        controls=[
                          Icon(
                            icons.VIDEO_CALL_OUTLINED,
                            size=20,
                            color=sb_ic
                          )
                        ]
                      )
                    ),


                    Container(
                      on_hover=self.sidebar_btn_hovered,
                      alignment=alignment.center,
                      height=s_btn_h,
                      width=s_btn_w,
                      border_radius=5,
                      content=Row(
                        spacing=0,
                        alignment='center',
                        controls=[
                          Icon(
                            icons.CALL_OUTLINED,
                            size=20,
                            color=sb_ic
                          )
                        ]
                      )
                    ),
                    
                    Container(
                      height=25,
                      width=2,
                      bgcolor=s_btn_h_c
                    ),
                    
                    Container(
                      on_hover=self.sidebar_btn_hovered,
                      alignment=alignment.center,
                      height=s_btn_h,
                      width=s_btn_w,
                      border_radius=5,
                      content=Row(
                        spacing=0,
                        alignment='center',
                        controls=[
                          Icon(
                            icons.SEARCH_OUTLINED,
                            size=20,
                            color=sb_ic
                          )
                        ]
                      )
                    ),

                  ]
                ),
              ]
            )

          ),
          
          Container(
            alignment=alignment.top_left,
            padding=padding.only(left=20,right=20,top=10),
            expand=True,
            image_src=wallpaper,
            image_opacity=0.2,
            image_fit=ImageFit.COVER,
            bgcolor='#1a343434',
            content=Column(
              scroll='auto',
              spacing=10,
              controls=[
                self.msg_obj,
              ]
            )

          ),
          
          Container(
            margin=margin.only(left=2),
            padding=padding.only(left=10,right=10),
            height=50,
            bgcolor=csc,
            content=Row(
              controls=[
                Container(
                  on_hover=self.sidebar_btn_hovered,
                  alignment=alignment.center,
                  height=40,
                  width=40,
                  border_radius=5,
                  content=Row(
                    spacing=0,
                    alignment='center',
                    controls=[
                      Icon(
                        icons.EMOJI_EMOTIONS_OUTLINED,
                        size=20,
                        color=sb_ic
                      )
                    ]
                  )
                ),
                
                Container(
                  on_hover=self.sidebar_btn_hovered,
                  alignment=alignment.center,
                  height=40,
                  width=40,
                  border_radius=5,
                  content=Row(
                    spacing=0,
                    alignment='center',
                    controls=[
                      Icon(
                        icons.PIN_INVOKE_SHARP,
                        size=20,
                        color=sb_ic
                      )
                    ]
                  )
                ),
                
                Container(
                  on_hover=self.sidebar_btn_hovered,
                  expand=True,
                  content=TextField(
                      expand=True,
                      multiline=True,
                      border=InputBorder.NONE,
                      hint_text='Type a message',
                      hint_style=TextStyle(
                        size=14,
                        font_family='arial',
                        color=htc
                      ),
                      color=sb_ic,
                      text_style=TextStyle(
                        size=14,
                        font_family='arial',
                        color=sb_ic
                      ),
                    ),
                  ),
                
                Container(
                  on_hover=self.sidebar_btn_hovered,
                  alignment=alignment.center,
                  height=40,
                  width=40,
                  border_radius=5,
                  content=Row(
                    spacing=0,
                    alignment='center',
                    controls=[
                      Icon(
                        icons.MIC_NONE_OUTLINED,
                        size=20,
                        color=sb_ic
                      )
                    ]
                  )
                ),

              ]
            )

          ),
        
        ]
      )
    )


t = App  
app(target=t,assets_dir='assets')
