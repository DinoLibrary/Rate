import os

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

drawable_dir = r"C:\khanhdt_dino\Rate\library\src\main\res\drawable"

emoji_base = """<vector xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:aapt="http://schemas.android.com/aapt"
    android:width="200dp"
    android:height="200dp"
    android:viewportWidth="200"
    android:viewportHeight="200">
    <!-- Base 3D Sphere shadow -->
    <path android:pathData="M100,105 m-95,0 a95,95 0 1,1 190,0 a95,95 0 1,1 -190,0" android:fillColor="#33000000" />
    <!-- Base 3D Sphere -->
    <path android:pathData="M100,100 m-95,0 a95,95 0 1,1 190,0 a95,95 0 1,1 -190,0">
        <aapt:attr name="android:fillColor">
            <gradient android:centerX="60" android:centerY="40" android:gradientRadius="160" android:type="radial">
                <item android:color="#FFFFE082" android:offset="0" />
                <item android:color="#FFFFB300" android:offset="1" />
            </gradient>
        </aapt:attr>
    </path>
    <!-- Top Highlight for Glass/3D effect -->
    <path android:pathData="M100,15 c-40,0 -70,20 -80,50 c15,-25 45,-40 80,-40 c35,0 65,15 80,40 c-10,-30 -40,-50 -80,-50 z">
        <aapt:attr name="android:fillColor">
            <gradient android:endY="65" android:startY="15" android:type="linear" android:startX="100" android:endX="100">
                <item android:color="#99FFFFFF" android:offset="0" />
                <item android:color="#00FFFFFF" android:offset="1" />
            </gradient>
        </aapt:attr>
    </path>
"""

emojis = {
    "rate_0": """
    <!-- Star Eyes -->
    <path android:pathData="M 60,35 L 68,55 L 88,58 L 73,72 L 78,92 L 60,82 L 42,92 L 47,72 L 32,58 L 52,55 Z" android:fillColor="#FF5252" />
    <path android:pathData="M 140,35 L 148,55 L 168,58 L 153,72 L 158,92 L 140,82 L 122,92 L 127,72 L 112,58 L 132,55 Z" android:fillColor="#FF5252" />
    <!-- Big Open Smile -->
    <path android:pathData="M 50,110 C 50,170 150,170 150,110 Z" android:fillColor="#3E2723" />
    <path android:pathData="M 70,140 C 70,130 130,130 130,140 C 130,165 70,165 70,140 Z" android:fillColor="#FF5252" />
    </vector>""",
    
    "rate_1": """
    <!-- Sad Eyes -->
    <path android:pathData="M 50,70 Q 70,50 90,70" android:strokeColor="#3E2723" android:strokeWidth="10" android:strokeLineCap="round"/>
    <path android:pathData="M 110,70 Q 130,50 150,70" android:strokeColor="#3E2723" android:strokeWidth="10" android:strokeLineCap="round"/>
    <!-- Crying Tears -->
    <path android:pathData="M 50,90 Q 50,120 70,120 Q 70,90 50,90" android:fillColor="#4FC3F7" />
    <path android:pathData="M 150,90 Q 150,120 130,120 Q 130,90 150,90" android:fillColor="#4FC3F7" />
    <!-- Sad Mouth -->
    <path android:pathData="M 60,150 Q 100,120 140,150" android:strokeColor="#3E2723" android:strokeWidth="12" android:strokeLineCap="round"/>
    </vector>""",
    
    "rate_2": """
    <!-- Disappointed Eyes -->
    <path android:pathData="M 50,60 L 80,75" android:strokeColor="#3E2723" android:strokeWidth="10" android:strokeLineCap="round"/>
    <path android:pathData="M 150,60 L 120,75" android:strokeColor="#3E2723" android:strokeWidth="10" android:strokeLineCap="round"/>
    <circle android:centerX="65" android:centerY="85" android:radius="8" android:fillColor="#3E2723" />
    <circle android:centerX="135" android:centerY="85" android:radius="8" android:fillColor="#3E2723" />
    <!-- Disappointed Mouth -->
    <path android:pathData="M 70,140 Q 100,130 130,140" android:strokeColor="#3E2723" android:strokeWidth="12" android:strokeLineCap="round"/>
    </vector>""",
    
    "rate_3": """
    <!-- Neutral Eyes -->
    <circle android:centerX="65" android:centerY="70" android:radius="10" android:fillColor="#3E2723" />
    <circle android:centerX="135" android:centerY="70" android:radius="10" android:fillColor="#3E2723" />
    <!-- Neutral Mouth -->
    <path android:pathData="M 60,130 L 140,130" android:strokeColor="#3E2723" android:strokeWidth="12" android:strokeLineCap="round"/>
    </vector>""",
    
    "rate_4": """
    <!-- Happy Eyes -->
    <path android:pathData="M 50,75 Q 65,55 80,75" android:strokeColor="#3E2723" android:strokeWidth="10" android:strokeLineCap="round"/>
    <path android:pathData="M 120,75 Q 135,55 150,75" android:strokeColor="#3E2723" android:strokeWidth="10" android:strokeLineCap="round"/>
    <!-- Smiling Mouth -->
    <path android:pathData="M 60,120 Q 100,160 140,120" android:strokeColor="#3E2723" android:strokeWidth="12" android:strokeLineCap="round"/>
    </vector>""",
    
    "rate_5": """
    <!-- Heart Eyes -->
    <path android:pathData="M 65,40 C 45,40 40,65 65,85 C 90,65 85,40 65,40 Z" android:fillColor="#E53935" />
    <path android:pathData="M 135,40 C 115,40 110,65 135,85 C 160,65 155,40 135,40 Z" android:fillColor="#E53935" />
    <!-- Big Smile -->
    <path android:pathData="M 50,110 C 50,160 150,160 150,110 Z" android:fillColor="#3E2723" />
    </vector>"""
}

# Write 3D Emojis
for name, content in emojis.items():
    write_file(os.path.join(drawable_dir, f"{name}.xml"), emoji_base + content)
    # Remove old png if exists
    png_path = os.path.join(drawable_dir, f"{name}.png")
    if os.path.exists(png_path):
        os.remove(png_path)

# 3D Pill Button (Rate)
btn_rate = """<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- Drop Shadow / Bottom 3D Bevel -->
    <item android:top="4dp">
        <shape android:shape="rectangle">
            <corners android:radius="50dp"/>
            <solid android:color="#C62828"/> <!-- Dark Red -->
        </shape>
    </item>
    <!-- Main Gradient Body -->
    <item android:bottom="4dp">
        <shape android:shape="rectangle">
            <corners android:radius="50dp"/>
            <gradient android:startColor="#FF9F43" android:endColor="#FF5252" android:angle="0"/>
        </shape>
    </item>
    <!-- Top Inner Highlight (Glassy 3D) -->
    <item android:bottom="4dp" android:top="2dp" android:left="4dp" android:right="4dp">
        <shape android:shape="rectangle">
            <corners android:radius="50dp"/>
            <stroke android:width="1dp" android:color="#44FFFFFF"/>
        </shape>
    </item>
</layer-list>
"""
write_file(os.path.join(drawable_dir, "rate_bg_button.xml"), btn_rate)

# Modern Card Background (dialog body)
card_bg = """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <corners android:radius="24dp" />
    <solid android:color="#FFFFFF" />
    <stroke android:width="1dp" android:color="#F0F0F0" />
</shape>
"""
write_file(os.path.join(drawable_dir, "rate_rounded_rectangle.xml"), card_bg)

# Cancel Button
btn_cancel = """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <corners android:radius="24dp" />
    <solid android:color="#F1F5F9" />
</shape>
"""
write_file(os.path.join(drawable_dir, "rate_bg_button_cancel.xml"), btn_cancel)

# Send Button
btn_send = """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <corners android:radius="24dp" />
    <solid android:color="#10B981" />
</shape>
"""
write_file(os.path.join(drawable_dir, "rate_bg_button_send.xml"), btn_send)

print("Generated all 3D XML assets successfully!")
