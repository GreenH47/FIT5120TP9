/****************************************************************************
 Copyright (c) 2010-2012 cocos2d-x.org
 Copyright (c) 2008-2010 Ricardo Quesada
 Copyright (c) 2011      Zynga Inc.

 http://www.cocos2d-x.org

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
 ****************************************************************************/
var _Score=0;
var _Index=1;
var _Max_Index=19;
var _Bg_ScaleRate=1;
var _P_ScaleRate=1;
var _arial;
var _notice_txt="";

var L_cs=cc.LayerColor.extend({
    bg:null,
    p1:null,
    p2:null,
    ljt1:null,
    ljt2:null,
    ljt3:null,
    ljt4:null,
    label_score:null,
    label_info:null,
    score:null,
    _plist:null,
    data_list:null,
    winSize:null,
    orgin:null,
    init:function(){

        this._super();
        this.score=0;
        this.setColor(cc.c3b(100,100,255));
        winsize=cc.Director.getInstance().getWinSize();
        orign=cc.Director.getInstance().getVisibleOrigin();

        

        var fullpath=cc.s_SharedFileUtils.fullPathForFilename(s_data_list);
        this._plist=cc.FileUtils.getInstance().createDictionaryWithContentsOfFile(fullpath);
        this.data_list=this._plist["cs"];


        this.bg=cc.Sprite.create(s_bg);
        _Bg_ScaleRate=winsize.height/this.bg.getBoundingBox().height;
        console.log(_Bg_ScaleRate);

        this.bg.setScaleX(_Bg_ScaleRate);
        this.bg.setScaleY(_Bg_ScaleRate);
        this.bg.setPosition(cc.p(orign.x+this.bg.getBoundingBox().width/2,orign.y+this.bg.getBoundingBox().height/2));

        this.label_score=cc.LabelTTF.create("Score:"+_Score,"Courier-Bold",33);
        this.label_score.setPosition(orign.x+winsize.width/2,orign.y+winsize.height*0.95);
        this.label_score.setColor(cc.c3b(255,148,0));
        this.label_info=cc.LabelTTF.create((this.data_list[_Index].name),"Courier-Bold",30);
        this.label_info.setPosition(orign.x+winsize.width/2,orign.y+winsize.height*0.7);



        this.ljt1=cc.Sprite.create(s_ljt_1);

        _P_ScaleRate=(winsize.width/this.ljt1.getBoundingBox().width)/4;

        this.ljt1.setScaleX(_P_ScaleRate);
        this.ljt1.setScaleY(_P_ScaleRate);
        this.ljt1.setPosition((cc.p(orign.x+this.ljt1.getBoundingBox().width/2,orign.y+this.ljt1.getBoundingBox().height/2+50*_P_ScaleRate)));
        this.addChild(this.ljt1,1);

        this.ljt2=cc.Sprite.create(s_ljt_2);
        this.ljt2.setScaleX(_P_ScaleRate);
        this.ljt2.setScaleY(_P_ScaleRate);
        this.ljt2.setPosition((cc.p(orign.x+this.ljt1.getBoundingBox().width*3/2,orign.y+this.ljt1.getBoundingBox().height/2+50*_P_ScaleRate)));
        this.addChild(this.ljt2,1);

        this.ljt3=cc.Sprite.create(s_ljt_3);
        this.ljt3.setScaleX(_P_ScaleRate);
        this.ljt3.setScaleY(_P_ScaleRate);
        this.ljt3.setPosition((cc.p(orign.x+this.ljt1.getBoundingBox().width*5/2,orign.y+this.ljt1.getBoundingBox().height/2+50*_P_ScaleRate)));
        this.addChild(this.ljt3,1);

        this.ljt4=cc.Sprite.create(s_ljt_4);
        this.ljt4.setScaleX(_P_ScaleRate);
        this.ljt4.setScaleY(_P_ScaleRate);
        this.ljt4.setPosition((cc.p(orign.x+this.ljt4.getBoundingBox().width*7/2,orign.y+this.ljt1.getBoundingBox().height/2+50*_P_ScaleRate)));
        this.addChild(this.ljt4,1);

        this.p1=cc.Sprite.create(this.data_list[_Index].img);
        this.p1.setScaleX(winsize.width/320);
        this.p1.setScaleY(winsize.width/320);
        this.p1.setPosition(winsize.width/2,winsize.height*2/3);


        this.addChild(this.bg,0);

        this.addChild(this.p1,2);
        this.addChild(this.label_score,0);
        this.addChild(this.label_info,4);
        this.schedule(this.touch_action);



        this.setTouchEnabled(true);

    },
    touch_action:function(){
        var p1point;
        p1point=this.p1.getPosition();
        if(cc.rectContainsPoint(this.ljt1.getBoundingBox(),p1point)){
            this.ljt1.setScaleX(_P_ScaleRate*1.1);
            this.ljt1.setScaleY(_P_ScaleRate*1.1);

        }else{
            this.ljt1.setScaleX(_P_ScaleRate);
            this.ljt1.setScaleY(_P_ScaleRate);
        }
        if(cc.rectContainsPoint(this.ljt2.getBoundingBox(),p1point)){
            this.ljt2.setScaleX(_P_ScaleRate*1.1);
            this.ljt2.setScaleY(_P_ScaleRate*1.1);

        }else{
            this.ljt2.setScaleX(_P_ScaleRate);
            this.ljt2.setScaleY(_P_ScaleRate);
        }

        if(cc.rectContainsPoint(this.ljt3.getBoundingBox(),p1point)){
            this.ljt3.setScaleX(_P_ScaleRate*1.1);
            this.ljt3.setScaleY(_P_ScaleRate*1.1);

        }else{
            this.ljt3.setScaleX(_P_ScaleRate);
            this.ljt3.setScaleY(_P_ScaleRate);
        }

        if(cc.rectContainsPoint(this.ljt4.getBoundingBox(),p1point)){
            this.ljt4.setScaleX(_P_ScaleRate*1.1);
            this.ljt4.setScaleY(_P_ScaleRate*1.1);

        }else{
            this.ljt4.setScaleX(_P_ScaleRate);
            this.ljt4.setScaleY(_P_ScaleRate);
        }
    },
    onTouchesBegan:function(touches,event){
        var touch=touches[0];
        var location=touch.getLocation();
        cc.log(location);
        if(cc.rectContainsPoint(this.p1.getBoundingBox(),location)){
            this.onClickFlag = true;
            cc.AudioEngine.getInstance().playMusic(s_delete_music,false);

        }


    },
    onTouchesMoved:function(touches,event){
        var touch = touches[0];
        var location = touch.getLocation();
        if(this.onClickFlag){
            this.p1.setPosition(location);
        }
    },

    onTouchesEnded:function(touches, event){
        this.onClickFlag = false;
        var p1point=this.p1.getPosition();
        if(cc.rectContainsPoint(this.ljt1.getBoundingBox(),p1point)||cc.rectContainsPoint(this.ljt2.getBoundingBox(),p1point)||cc.rectContainsPoint(this.ljt3.getBoundingBox(),p1point)||cc.rectContainsPoint(this.ljt4.getBoundingBox(),p1point)){
            cc.AudioEngine.getInstance().playMusic(s_delete_music,false);
            var _right=false;
            if((cc.rectContainsPoint(this.ljt1.getBoundingBox(),p1point)&&this.data_list[_Index].class==1)){
                _Score+=1;
                _right=true;
            }
            if((cc.rectContainsPoint(this.ljt2.getBoundingBox(),p1point)&&this.data_list[_Index].class==2)){
                _Score+=1;
                _right=true;
            }
            if((cc.rectContainsPoint(this.ljt3.getBoundingBox(),p1point)&&this.data_list[_Index].class==3)){
                _Score+=1;
                _right=true;
            }
            if((cc.rectContainsPoint(this.ljt4.getBoundingBox(),p1point)&&this.data_list[_Index].class==4)){
                _Score+=1;
                _right=true;
            }

            if(!_right){
                _notice_txt+=this.data_list[_Index].name+" belong to "+this.trans_index_to_class(this.data_list[_Index].class)+"\n";
            }

            if(_Index<_Max_Index){
                _Index+=1;
            }else{
                var _scene=new Scene_end();
                cc.Director.getInstance().replaceScene(cc.TransitionFade.create(1.0,_scene));
            }

            this.label_score.setString("Score:"+_Score);
            //console.log(_Score);
            var actionScale1=cc.ScaleTo.create(0.2,0.1,0,1);
            var actionFadeOut=cc.FadeOut.create(0.2);
            var action1=cc.Spawn.create(actionScale1,actionFadeOut);
            this.p1.runAction(cc.Sequence.create(action1,cc.DelayTime.create(0.2)));
            var actionScale2=cc.ScaleTo.create(0.2,1,1);
            var actionFadeIn=cc.FadeIn.create(0.2);
            var action2=cc.Spawn.create(actionScale2,actionFadeIn);
            //this.removeChild(this.p1);
            this.p1=cc.Sprite.create(this.data_list[_Index].img);
            this.p1.setPosition(cc.p(winsize.width/2,winsize.height*2/3));
            this.p1.setOpacity(0);
            this.p1.setScaleX(winsize.width/320);
            this.p1.setScaleY(winsize.width/320);
            this.addChild(this.p1,2);
            this.p1.runAction(action2);
            this.label_info.setString(this.data_list[_Index].name);

        }
    },
    trans_index_to_class:function(_index){
        switch(_index){
            case 1: return "kitchen waste";
                break;
            case 2: return "recyclable";
                break;
            case 3: return "hazardous waste";
                break;
            case 4: return "other waste";
                break;
            case 5: return "不可烂垃圾";
                break;
            case 6: return "可烂垃圾";
                break;
        }
    }
});
var L_xc=cc.LayerColor.extend({
    bg:null,
    p1:null,
    p2:null,
    ljt5:null,
    ljt6:null,

    label_score:null,
    label_info:null,
    score:null,
    _plist:null,
    data_list:null,
    winSize:null,
    orgin:null,
    init:function(){

        this._super();
        this.score=0;
        this.setColor(cc.c3b(100,100,255));
        winsize=cc.Director.getInstance().getWinSize();
        orign=cc.Director.getInstance().getVisibleOrigin();



        var fullpath=cc.s_SharedFileUtils.fullPathForFilename(s_data_list);
        this._plist=cc.FileUtils.getInstance().createDictionaryWithContentsOfFile(fullpath);
        this.data_list=this._plist["nc"];


        this.bg=cc.Sprite.create(s_bg);
        _Bg_ScaleRate=winsize.height/this.bg.getBoundingBox().height;
        console.log(_Bg_ScaleRate);

        this.bg.setScaleX(_Bg_ScaleRate);
        this.bg.setScaleY(_Bg_ScaleRate);
        this.bg.setPosition(cc.p(orign.x+this.bg.getBoundingBox().width/2,orign.y+this.bg.getBoundingBox().height/2));

        this.label_score=cc.LabelTTF.create("Score:"+_Score,"Courier-Bold",33);
        this.label_score.setPosition(orign.x+winsize.width/2,orign.y+winsize.height*0.95);
        this.label_score.setColor(cc.c3b(255,148,0));
        this.label_info=cc.LabelTTF.create((this.data_list[_Index].name),"Courier-Bold",30);
        this.label_info.setPosition(orign.x+winsize.width/2,orign.y+winsize.height*0.7);



        this.ljt5=cc.Sprite.create(s_ljt_5);

        _P_ScaleRate=(winsize.width/this.ljt5.getBoundingBox().width)/3;

        this.ljt5.setScaleX(_P_ScaleRate);
        this.ljt5.setScaleY(_P_ScaleRate);
        this.ljt5.setPosition((cc.p(orign.x+winsize.width/6+this.ljt5.getBoundingBox().width/2,orign.y+this.ljt5.getBoundingBox().height/2+50*_P_ScaleRate)));
        this.addChild(this.ljt5,1);

        this.ljt6=cc.Sprite.create(s_ljt_6);
        this.ljt6.setScaleX(_P_ScaleRate);
        this.ljt6.setScaleY(_P_ScaleRate);
        this.ljt6.setPosition((cc.p(orign.x+winsize.width/6+this.ljt5.getBoundingBox().width*3/2,orign.y+this.ljt5.getBoundingBox().height/2+50*_P_ScaleRate)));
        this.addChild(this.ljt6,1);



        this.p1=cc.Sprite.create(this.data_list[_Index].img);
        this.p1.setScaleX(winsize.width/320);
        this.p1.setScaleY(winsize.width/320);
        this.p1.setPosition(winsize.width/2,winsize.height*2/3);


        this.addChild(this.bg,0);

        this.addChild(this.p1,2);
        this.addChild(this.label_score,0);
        this.addChild(this.label_info,4);
        this.schedule(this.touch_action);


        this.setTouchEnabled(true);

    },
    touch_action:function(){
        var p1point;
        p1point=this.p1.getPosition();
        if(cc.rectContainsPoint(this.ljt5.getBoundingBox(),p1point)){
            this.ljt5.setScaleX(_P_ScaleRate*1.1);
            this.ljt5.setScaleY(_P_ScaleRate*1.1);

        }else{
            this.ljt5.setScaleX(_P_ScaleRate);
            this.ljt5.setScaleY(_P_ScaleRate);
        }
        if(cc.rectContainsPoint(this.ljt6.getBoundingBox(),p1point)){
            this.ljt6.setScaleX(_P_ScaleRate*1.1);
            this.ljt6.setScaleY(_P_ScaleRate*1.1);

        }else{
            this.ljt6.setScaleX(_P_ScaleRate);
            this.ljt6.setScaleY(_P_ScaleRate);
        }



    },
    onTouchesBegan:function(touches,event){
        var touch=touches[0];
        var location=touch.getLocation();
        cc.log(location);
        if(cc.rectContainsPoint(this.p1.getBoundingBox(),location)){
            this.onClickFlag = true;
            cc.AudioEngine.getInstance().playMusic(s_delete_music,false);
        }


    },
    onTouchesMoved:function(touches,event){
        var touch = touches[0];
        var location = touch.getLocation();
        if(this.onClickFlag){
            this.p1.setPosition(location);
        }
    },

    onTouchesEnded:function(touches, event){
        this.onClickFlag = false;
        var p1point=this.p1.getPosition();
        if(cc.rectContainsPoint(this.ljt5.getBoundingBox(),p1point)||cc.rectContainsPoint(this.ljt6.getBoundingBox(),p1point)){
            cc.AudioEngine.getInstance().playMusic(s_delete_music,false);
            var _right=false;
            if(cc.rectContainsPoint(this.ljt5.getBoundingBox(),p1point)&&this.data_list[_Index].class==5){
                _Score+=1;
                _right=true;
            }
            if(cc.rectContainsPoint(this.ljt6.getBoundingBox(),p1point)&&this.data_list[_Index].class==6){
                _Score+=1;
                _right=true;
            }
            if(!_right){
                _notice_txt+=this.data_list[_Index].name+"belong to"+this.trans_index_to_class(this.data_list[_Index].class)+"\n";
            }
            if(_Index<_Max_Index){
                _Index+=1;
            }else{
                var _scene=new Scene_end();
                cc.Director.getInstance().replaceScene(cc.TransitionFade.create(1.0,_scene));
            }

            this.label_score.setString("Score:"+_Score);
            //console.log(_Score);
            var actionScale1=cc.ScaleTo.create(0.2,0.1,0,1);
            var actionFadeOut=cc.FadeOut.create(0.2);
            var action1=cc.Spawn.create(actionScale1,actionFadeOut);
            this.p1.runAction(cc.Sequence.create(action1,cc.DelayTime.create(0.2)));
            var actionScale2=cc.ScaleTo.create(0.2,1,1);
            var actionFadeIn=cc.FadeIn.create(0.2);
            var action2=cc.Spawn.create(actionScale2,actionFadeIn);
            //this.removeChild(this.p1);
            this.p1=cc.Sprite.create(this.data_list[_Index].img);
            this.p1.setPosition(cc.p(winsize.width/2,winsize.height*2/3));
            this.p1.setOpacity(0);
            this.p1.setScaleX(winsize.width/320);
            this.p1.setScaleY(winsize.width/320);
            this.addChild(this.p1,2);
            this.p1.runAction(action2);
            this.label_info.setString(this.data_list[_Index].name);

        }
    },

    trans_index_to_class:function(_index){
        switch(_index){
            case 1: return "kitchen waste";
            break;
            case 2: return "recyclable";
            break;
            case 3: return "hazardous waste";
            break;
            case 4: return "other waste";
            break;
            case 5: return "不可烂垃圾";
            break;
            case 6: return "可烂垃圾";
            break;
        }
    }

});
var Main_layer=cc.LayerColor.extend({
    fm:null,
    winsize:null,
    orign:null,
    init:function(){
        this._super();
        this.setColor(cc.c3b(0,255,0));

        document.title="Life waste classification";
        this.winsize=cc.Director.getInstance().getWinSize();
        this.orign=cc.Director.getInstance().getVisibleOrigin();

        this.fm=cc.Sprite.create(s_fm);
        this.fm.setScaleX(this.winsize.width/this.fm.getBoundingBox().width);
        this.fm.setScaleY(this.winsize.height/this.fm.getBoundingBox().height);
        this.fm.setPosition(cc.p(this.orign.x+this.fm.getBoundingBox().width/2,this.orign.y+this.fm.getBoundingBox().height/2));

        cc.MenuItemFont.setFontName("Arial");

        var title_label = cc.LabelTTF.create("Waste classification", "Arial", 50);
        title_label.setColor(cc.c3b(255, 148, 0));
        title_label.setPosition(this.winsize.width / 2, this.winsize.height - 100); // position it at the top of the screen with a little margin
        this.addChild(title_label, 2); 

        var main_label=cc.LabelTTF.create("I want to test","Arial",40);
        main_label.setVisible(false);

        var xc_label=cc.LabelTTF.create("Test","Arial",40);
        xc_label.setColor(cc.c3b(255,148,0));
        xc_label.setVisible(false);

        var learn_label=cc.LabelTTF.create("I want to study","Arial",40);
        learn_label.setColor(cc.c3b(255,148,0));
        learn_label.setVisible(false);

        var cs_label=cc.LabelTTF.create("Start the game","Arial",40);
        cs_label.setColor(cc.c3b(255,148,0));

        var menuItem0=cc.MenuItemLabel.create(main_label,this.main_select,this);
        var menuItem1=cc.MenuItemLabel.create(cs_label,this.cs_select,this);
        var menuItem2=cc.MenuItemLabel.create(xc_label,this.xc_select,this);
        var menuItem3=cc.MenuItemLabel.create(learn_label,this.learn_select,this);

        menuItem1.setPosition(cc.p(menuItem0.getPosition().x,menuItem0.getPosition().y-60));
        menuItem2.setPosition(cc.p(menuItem1.getPosition().x,menuItem1.getPosition().y-1000));
        menuItem3.setPosition(cc.p(menuItem2.getPosition().x,menuItem2.getPosition().y-1000));

        var menu=cc.Menu.create();
        menu.addChild(menuItem0);
        menu.addChild(menuItem1);
        menu.addChild(menuItem2);
        menu.addChild(menuItem3);

        //menu.alignItemsVerticallyWithPadding(10);
        menu.setPosition(cc.p(this.winsize.width/2,this.winsize.height*3/4));
        menu.setColor(cc.c3b(255,148,0));
        this.addChild(this.fm,0);
        this.addChild(menu,1);

    },
    main_select: function () {

    },
    learn_select: function () {
        cc.AudioEngine.getInstance().playMusic(s_delete_music,false);
        var _scene=new Scene_learn();
        cc.Director.getInstance().replaceScene(cc.TransitionFade.create(1.0,_scene));
    },
    cs_select:function(pSender){
        cc.AudioEngine.getInstance().playMusic(s_delete_music,false);
        _arial="Australia";
        var _scene=new Scene_cs();
        cc.Director.getInstance().replaceScene(cc.TransitionFade.create(1.0,_scene));
    },
    xc_select:function(pSender){
        cc.AudioEngine.getInstance().playMusic(s_delete_music,false);
        _arial="Test";
        var _scene=new Scene_xc();
        cc.Director.getInstance().replaceScene(cc.TransitionFade.create(1.0,_scene));
    }
});
var L_end=cc.LayerColor.extend({
    info_Label1:null,
    info_Label2:null,
    winsize:null,
    orign:null,
    info_notice:null,
    init:function(){
        this._super();
        this.setColor(cc.c3b(0,153,204));
        this.winsize=cc.Director.getInstance().getWinSize();
        this.orign=cc.Director.getInstance().getVisibleOrigin();
        var _percent=parseInt(_Score*100/_Max_Index);
        var _words;
        if(_percent>=90){
            _words="Perfect!";
        }else if(_percent>=70){
            _words="Great!";
        }else if(_percent>=50){
            _words="Good!";
        }else{
            _words="Not good!";
        }
        this.info_Label1=cc.LabelTTF.create("Your score is "+_Score+", the accuracy is "+_percent+"%","Arial",30);
        this.info_Label1.setPosition(orign.x+winsize.width/2,orign.y+winsize.height*3/7);
        this.info_Label2=cc.LabelTTF.create(" "+_words,"Arial",25);
        this.info_Label2.setPosition(orign.x+winsize.width/2,orign.y+winsize.height*3/7-30);

        this.info_notice=cc.LabelTTF.create(_notice_txt,"Arial",20);
        //this.info_notice.setPosition(orign.x+this.info_notice.getBoundingBox().width/2,winsize.height-this.info_notice.getBoundingBox().height/2);

        this.info_notice.setPosition(orign.x+this.winsize.width/2,winsize.height-this.info_notice.getBoundingBox().height/2-20);

        this.info_notice.setColor(cc.c3b(255,255,255));

        var retry_label=cc.LabelTTF.create("Play again","Arial",40);

        retry_label.setColor(cc.c3b(255,148,0));
        var menuItem0=cc.MenuItemLabel.create(retry_label,this.retry_selected,this);
        var menu=cc.Menu.create();
        menu.addChild(menuItem0,1);
        menu.setPosition(cc.p(orign.x+winsize.width/2,orign.y+winsize.height*3/7-60));

        this.addChild(this.info_Label1,1);
        this.addChild(this.info_Label2,1);
        this.addChild(this.info_notice,0);
        this.addChild(menu,1);
        document.title="I just try"+_arial+"waste classification and my accuracy is"+_percent+"%!";
        },
    retry_selected:function(pSender){
        var _scene=new MyScene();
        _Index=1;
        _Score=0;
        _notice_txt="";
        cc.Director.getInstance().replaceScene(cc.TransitionFade.create(1.0,_scene));
    }

});
var L_learn=cc.LayerColor.extend({
    p_learn:null,
    o_location:null,
    o_position:null,
    winsize:null,
    orign:null,
    init:function(){
        this._super();
        this.setColor(cc.c3b(0,255,0));
        this.p_learn=cc.Sprite.create(s_learn);
        this.winsize=cc.Director.getInstance().getWinSize();
        this.orign=cc.Director.getInstance().getVisibleOrigin();
        this.p_learn.setScaleX(this.winsize.width/this.p_learn.getBoundingBox().width);
        this.p_learn.setScaleY(this.winsize.width/600);
        this.p_learn.setPosition(this.winsize.width/2,this.winsize.height-this.p_learn.getBoundingBox().height/2);
        this.addChild(this.p_learn,0);

        var back_label=cc.LabelTTF.create("Back","Arial",30);
        back_label.setColor(cc.c3b(255,255,255));
        var menuItem0=cc.MenuItemLabel.create(back_label,this.back_selected,this);
        var menu=cc.Menu.create();
        menu.addChild(menuItem0);
        menu.setPosition(cc.p(this.orign.x+this.winsize.width/2,this.orign.y+back_label.getBoundingBox().height/2+20));
        this.addChild(menu,1);


        this.setTouchEnabled(true);
},
    back_selected:function(pSender){
        var _scene=new MyScene();
        _Index=1;
        _Score=0;
        cc.Director.getInstance().replaceScene(cc.TransitionFade.create(1.0,_scene));
    },
    onTouchesBegan:function(touches,event){
        var touch=touches[0];
        var location=touch.getLocation();
        cc.log(location);
        if(cc.rectContainsPoint(this.p_learn.getBoundingBox(),location)){
            this.onClickFlag = true;
            this.o_position=this.p_learn.getPosition().y;
            this.o_location=location.y;
        }


    },
    onTouchesMoved:function(touches,event){
        var touch = touches[0];
        var location = touch.getLocation();
        if(this.onClickFlag){
            this.p_learn.setPosition(cc.p(this.p_learn.getPosition().x, this.o_position + location.y - this.o_location));
            if(this.p_learn.getPosition().y<this.winsize.height-this.p_learn.getBoundingBox().height/2) {
                this.p_learn.setPosition(this.winsize.width/2,this.winsize.height-this.p_learn.getBoundingBox().height/2);
            }
            if(this.p_learn.getPosition().y>this.p_learn.getBoundingBox().height/2) {
                this.p_learn.setPosition(this.winsize.width/2,this.p_learn.getBoundingBox().height/2);
            }

        }
    },

    onTouchesEnded:function(touches, event){
        this.onClickFlag = false;

    }

});
var Scene_learn=cc.Scene.extend({
    onEnter: function () {
        this._super();
        var layer=new L_learn();
        this.addChild(layer);
        layer.init();
    }
});
var Scene_end=cc.Scene.extend({
    onEnter:function(){
        this._super();
        var layer=new L_end();
        this.addChild(layer);
        layer.init();
    }
});
var Scene_xc=cc.Scene.extend({
    onEnter:function(){
        this._super();
        var layer=new L_xc();
        this.addChild(layer);
        layer.init();
    }
});
var Scene_cs=cc.Scene.extend({
    onEnter:function(){
        this._super();
        var layer=new L_cs();
        this.addChild(layer);
        layer.init();
    }

});
var MyScene = cc.Scene.extend({

    onEnter:function () {
        this._super();

        var layer = new Main_layer();

        this.addChild(layer);
        layer.init();
    }
});
