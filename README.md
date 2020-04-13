<p align="center"> 
<img src="images/islamic.png" style="float: left" width=15%/>
<img src="images/b0.png" style="float: center" width=50%/>
<img src="images/islamic.png" style="float: right" width=15%/>
</p>

<br>

تحتوي هذه الصفحة على جميع التعليمات لتثبيت الحزم المطلوبة للمشاريع القادمة


اتبع تلك التعليمات اثناء مشاهدة فيديو الشرح 

[**تجهيز البيئة الافتراضية**](#1-تجهيز-البيئة-الافتراضية) &nbsp;**|**&nbsp;
[**dlib**](#2-dlib) &nbsp;**|**&nbsp;
[**face-recognition**](#3-face-recognition) &nbsp;**|**&nbsp;
[**cvlib**](#4-cvlib)


# 1. تجهيز البيئة الافتراضية

 [فقرأ هذا](https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners#setup) `anaconda` اذا لم تكن تمتلك

إذا كان `إصدار بايثون الخاص بك ليس 3.6` ، فاتبع هذا القسم وإلا تابع إلى القسم التالي

## وافتحه `anaconda prompt` ابحث عن هذه البرنامج  
(بأي اسم تريده `YOUR_ENVIRONMENT_NAME` إنشاء بيئة افتراضية (استبدل <br>

    conda create -n YOUR_ENVIRONMENT_NAME python=3.6

قم بتفعيل تلك البيئة
    
    conda activate YOUR_ENVIRONMENT_NAME


# 2. [dlib](http://pypi.fcio.net/simple/dlib/)

### خطوة #1

    pip install http://pypi.fcio.net/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#md5=9a704406fbb4036f70b5f174fec9db1f

---
إذا حدثت أي أخطاء عندئذٍ <br>

### خطوة #2 

[cmake](https://cmake.org/download/) قم بتثبيت 

ثم قم بـــــ
    
    pip install cmake 

بعد ذلك أعد خطوة #1

---
إذا حدثت أي أخطاء عندئذٍ <br>

### خطوة #3
قم بتثبيت [Visual Studio 2015](https://visualstudio.microsoft.com/vs/older-downloads/)

بعد ذلك أعد خطوة #1


# 3. face-recognition

 بشكل صحيح [dlib](#2-dlib) لذا تأكد من تثبيت [dlib](#2-dlib) تعتمد هذه الحزمة على  

    pip install face-recognition

في الفيديو لقد استخدمت
    
    pip install face_recognition

ولكن أى واحد من تلك الأوامر سوف يوم بتثبيت نفس المكتبة 

# 4. [cvlib](https://github.com/arunponnusamy/cvlib)

    pip install opencv-python tensorflow

    pip install cvlib
`AMD gpu` وليس `Nvidia gpu` قم بتشغيل الأمر التالي فقط اذا كان لديك كارت شاشة 
 
    pip install tensorflow-gpu


![](images/hamd.png)