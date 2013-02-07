#! /Applications/Nuke6.0v1-32/Nuke6.0v1.app/Contents/MacOS/Nuke6.0v1 -nx
version 6.0 v1
Gizmo {
 addUserKnob {20 User}
 addUserKnob {6 chromaticenable l "chromatic aberration" +STARTLINE}
 addUserKnob {41 mix l "color mix" T mixer.mix}
 addUserKnob {41 presaturation l "pre saturation" T Saturation1.saturation}
 addUserKnob {41 saturation l "post saturation" T Saturation_post.saturation}
 addUserKnob {20 threecolorgroup l "3 color process" n 1}
 threecolorgroup 0
 addUserKnob {41 value l surpress T Multiply1.value}
 addUserKnob {41 hue_rotation l "hue shift" T HueShift_3color.hue_rotation}
 addUserKnob {20 endGroup_1 l endGroup n -1}
 addUserKnob {20 twocolorgroup l "2 color process" n 1}
 twocolorgroup 0
 addUserKnob {41 translate l "shift cyan" T cyan_shift.translate}
 addUserKnob {41 hue_rotation_1 l "hue rotation" T HueShift_2color.hue_rotation}
 addUserKnob {41 mix_1 l "add yellow" T yello_mixer.mix}
 addUserKnob {20 endGroup_2 l endGroup n -1}
 addUserKnob {20 blacklevelsgroup l "black levels" n 1}
 blacklevelsgroup 0
 addUserKnob {41 contrast T RolloffContrast1.contrast}
 addUserKnob {41 center T RolloffContrast1.center}
 addUserKnob {41 minimum T Clamp1.minimum}
 addUserKnob {41 soft_clip l "soft clip" T RolloffContrast1.soft_clip}
 addUserKnob {20 endGroup_3 l endGroup n -1}
 addUserKnob {41 mix_2 l mix T finalmix.mix}
 addUserKnob {26 ""}
 addUserKnob {26 info l "" -STARTLINE T "Retro! v0.4  Julian van Mil, 2010"}
 addUserKnob {20 chromotic l "chromatic aberration"}
 addUserKnob {41 multiplier l amount T Dot8.multiplier}
 addUserKnob {41 mixRay l "mix rays" T moxDot.mixRay}
 addUserKnob {41 size l blur T Blur1.size}
 addUserKnob {41 which T Switch1.which}
 addUserKnob {6 radialmaskcheck l "radial mask" +STARTLINE}
 addUserKnob {20 radialmaskgroup l "radial mask fine tune" n 1}
 radialmaskgroup 0
 addUserKnob {41 scale T Transform_radial.scale}
 addUserKnob {41 blackpoint T Grade_radial.blackpoint}
 addUserKnob {41 whitepoint T Grade_radial.whitepoint}
 addUserKnob {41 opacity T Radial1.opacity}
 addUserKnob {20 endGroup n -1}
 addUserKnob {20 about l info t information}
 addUserKnob {26 information l "" +STARTLINE T "Retro! simulates 2 and 3 color strip processes from the ealry days of color film.\n\nRetro! is really just a Nuke port of the fantastic 'Oldify' for shake by BrainFaucet.\nChromatic Aberration effect borrowed from Donald Strubler's st.Rub's akromatism\n\nFrom original 'Oldify' description;\nThis macro attempts to make footage look like it\nwas shot with older film processes.  \nThis is based on the technicolor work done for Aviator though \nit transformed into a much more\nempirically based approach and less of a\ntechnical approach.\n\nThere is the 3 color process as well as a 2 color\nprocess.  A ColorMixer property mixes between\nthese two processes.  This mixing isn't based\non anything but does give some rather good\nlooks. There is also yellow dye and black level\ncontrols."}
}
 BackdropNode {
  inputs 0
  name BackdropNode1
  tile_color 0x232323ff
  label "2 COLOR"
  note_font_size 25
  xpos -161
  ypos -60
  bdwidth 328
  bdheight 486
 }
 BackdropNode {
  inputs 0
  name BackdropNode2
  tile_color 0x131313ff
  label "3 COLOR"
  note_font_size 22
  xpos 183
  ypos -60
  bdwidth 248
  bdheight 484
 }
 BackdropNode {
  inputs 0
  name BackdropNode3
  label CHROMATIC
  note_font_size 22
  xpos 559
  ypos 791
  bdwidth 701
  bdheight 535
 }
 Dot {
  inputs 0
  name Dot8
  xpos 657
  ypos 957
  addUserKnob {20 User}
  addUserKnob {7 multiplier R -0.1 0.1}
  multiplier -0.02
 }
 Input {
  inputs 0
  name Input1
  xpos 60
  ypos -242
 }
 Dot {
  name Dot4
  xpos 94
  ypos -123
 }
set N1c60f260 [stack 0]
 Dot {
  name Dot2
  xpos 510
  ypos -123
 }
 Dot {
  name Dot3
  xpos 510
  ypos 668
 }
push $N1c60f260
 Saturation {
  name Saturation1
  xpos 60
  ypos -91
 }
 RolloffContrast {
  contrast 1.1
  center 0.3
  slope_mag_low1 0.8000000119
  black_low 1
  slope_mag_high2 0.8000000119
  white_high 1
  name RolloffContrast1
  xpos 60
  ypos -14
 }
set N1e026e0 [stack 0]
 Dot {
  name Dot5
  xpos 253
  ypos -11
 }
 HueShift {
  name HueShift_3color
  xpos 219
  ypos 48
 }
 Expression {
  expr0 r-max(g,b)
  expr1 g-max(r,b)
  expr2 b-max(r,g)
  name difference_exp
  xpos 219
  ypos 91
 }
 Multiply {
  name Multiply1
  xpos 219
  ypos 125
 }
 Expression {
  expr3 max(r,max(g,b))
  name create_alpah_exp
  xpos 219
  ypos 177
 }
push $N1e026e0
 Dot {
  name Dot1
  xpos 363
  ypos -11
 }
 Merge2 {
  inputs 2
  name Merge5
  xpos 329
  ypos 177
 }
 Dot {
  name Dot6
  xpos 363
  ypos 367
 }
push $N1e026e0
 HueShift {
  hue_rotation 3
  name HueShift_2color
  xpos -55
  ypos -14
 }
 Expression {
  expr0 r
  expr1 (g+b)/2
  expr2 (g+b)/2
  name cyan_and_red_exp
  xpos -132
  ypos 96
 }
set N193c0060 [stack 0]
 Expression {
  expr0 (r+g)/2
  expr1 (r+g)/2
  expr2 0
  name yellow_dye
  xpos 31
  ypos 96
 }
push $N193c0060
 Merge2 {
  inputs 2
  mix 0.11
  name yello_mixer
  xpos -55
  ypos 189
 }
set N193d61e0 [stack 0]
 Transform {
  translate {0.5 0.5}
  center {1024 778}
  name cyan_shift
  xpos 55
  ypos 189
 }
push $N193d61e0
 Copy {
  inputs 2
  from0 rgba.green
  to0 rgba.green
  from1 rgba.blue
  to1 rgba.blue
  name Copy_cyan
  xpos -55
  ypos 353
 }
 Merge2 {
  inputs 2
  mix 0.3
  name mixer
  xpos 108
  ypos 364
 }
 Clamp {
  minimum 0.01
  maximum 5
  maximum_enable false
  name Clamp1
  xpos 108
  ypos 507
 }
 ShuffleCopy {
  inputs 2
  name ShuffleCopy3
  xpos 108
  ypos 665
 }
set N193e2b00 [stack 0]
 Dot {
  name Dot9
  xpos 901
  ypos 668
 }
 Dot {
  name Dot7
  xpos 901
  ypos 846
 }
set N193e9940 [stack 0]
 Remove {
  name Remove1
  xpos 1097
  ypos 838
 }
 Radial {
  cliptype none
  area {0 0 {format.width i} {format.height i}}
  softness 0.18
  name Radial1
  xpos 1097
  ypos 918
  hide_input true
 }
 Transform {
  center {{format.width/2 i} {format.height/2 i}}
  name Transform_radial
  xpos 1097
  ypos 942
 }
 Blur {
  size 300
  quality 30
  name Blur3
  xpos 1097
  ypos 967
 }
 Grade {
  channels {rgba.red rgba.green rgba.blue rgba.alpha}
  blackpoint 0.095
  whitepoint 1.02
  black 0.003
  name Grade_radial
  xpos 1097
  ypos 1027
 }
 Dot {
  name Dot13
  xpos 1131
  ypos 1146
 }
push $N193e9940
 Dot {
  name Dot12
  xpos 692
  ypos 846
 }
push $N193e9940
 GodRays {
  channels {-rgba.red rgba.green -rgba.blue}
  scale {{parent.GodRays8.scale}}
  center {{parent.GodRays5.center.x} {parent.GodRays5.center.y}}
  name GodRays6
  xpos 980
  ypos 918
 }
 GodRays {
  channels {rgba.red -rgba.green -rgba.blue}
  scale {{parent.GodRays5.scale}}
  center {{parent.GodRays6.center.x} {parent.GodRays6.center.y}}
  name GodRays7
  xpos 980
  ypos 1007
  addUserKnob {20 User}
  addUserKnob {4 sasdasd M {Read1 ""}}
 }
push $N193e9940
 GodRays {
  channels {-rgba.red -rgba.green rgba.blue}
  scale {{(Dot8.multiplier)+1 i}}
  center {{(format.width)/2 i x1 400} {(format.height)/2 i}}
  name GodRays8
  xpos 867
  ypos 918
 }
 GodRays {
  channels {-rgba.red rgba.green -rgba.blue}
  scale {{parent.GodRays2.scale i}}
  center {{parent.GodRays8.center.x i} {parent.GodRays8.center.y i}}
  name GodRays5
  xpos 867
  ypos 1008
  addUserKnob {20 User}
  addUserKnob {4 sasdasd M {Read1 ""}}
 }
push $N193e9940
 GodRays {
  channels {-rgba.red -rgba.green rgba.blue}
  scale {{(Dot8.multiplier)+1 i}}
  center {{(format.width)/2 i} {(format.height)/2 i}}
  name GodRays1
  xpos 752
  ypos 921
 }
 GodRays {
  channels {rgba.red -rgba.green -rgba.blue}
  scale {{((Dot8.multiplier)*(-1))+1 i}}
  center {{parent.GodRays1.center.x i} {parent.GodRays1.center.y i}}
  name GodRays2
  xpos 752
  ypos 1006
  addUserKnob {20 User}
  addUserKnob {4 sasdasd M {Read1 ""}}
 }
 Switch {
  inputs 3
  which 2
  name Switch1
  xpos 867
  ypos 1079
  addUserKnob {20 User}
  addUserKnob {41 which_1 l which T Switch1.which}
 }
 GodRays {
  scale {{((moxDot.mixRay)*.05)+1 i}}
  center {{width/2 i} {height/2 i}}
  name GodRays3
  xpos 867
  ypos 1131
  addUserKnob {20 User}
  addUserKnob {7 mult}
  mult 1
 }
 Blur {
  size 1
  name Blur1
  xpos 867
  ypos 1214
 }
 Keymix {
  inputs 3
  name Keymix_radial
  xpos 658
  ypos 1214
  disable {{!parent.radialmaskcheck i}}
 }
push $N193e2b00
 Switch {
  inputs 2
  which 1
  name Switch2
  xpos 108
  ypos 1219
  disable {{!parent.chromaticenable i}}
 }
 Saturation {
  name Saturation_post
  xpos 108
  ypos 1243
 }
push $N1c60f260
 Dot {
  name Dot11
  xpos -456
  ypos -123
 }
 Dot {
  name Dot10
  xpos -456
  ypos 1288
 }
 Merge2 {
  inputs 2
  name finalmix
  xpos 108
  ypos 1285
 }
 Output {
  name Output1
  xpos 108
  ypos 1437
 }
 Dot {
  inputs 0
  name moxDot
  xpos 1014
  ypos 1139
  addUserKnob {20 User}
  addUserKnob {7 mixRay}
  mixRay 0.05
 }
end_group
