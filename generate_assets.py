import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

def circle_path(cx, cy, r, color):
    return f'<path android:pathData="M {cx},{cy} m -{r},0 a {r},{r} 0 1,0 {r*2},0 a {r},{r} 0 1,0 -{r*2},0" android:fillColor="{color}" />'

script_dir = os.path.dirname(os.path.abspath(__file__))
drawable_dir = os.path.join(script_dir, "library", "src", "main", "res", "drawable")

emoji_base = """<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:aapt="http://schemas.android.com/aapt"
    android:width="200dp"
    android:height="200dp"
    android:viewportWidth="200"
    android:viewportHeight="200">
    <!-- Ambient Drop Shadow -->
    <path android:pathData="M100,106 m-90,0 a90,90 0 1,1 180,0 a90,90 0 1,1 -180,0" android:fillColor="#26000000" />
    
    <!-- Base 3D Sphere with Rich Radial Gradient -->
    <path android:pathData="M100,100 m-92,0 a92,92 0 1,1 184,0 a92,92 0 1,1 -184,0">
        <aapt:attr name="android:fillColor">
            <gradient android:centerX="65" android:centerY="45" android:gradientRadius="165" android:type="radial">
                <item android:color="#FFFFFAEC" android:offset="0.0" />
                <item android:color="#FFFFD54F" android:offset="0.25" />
                <item android:color="#FFFFB300" android:offset="0.70" />
                <item android:color="#FFFF8F00" android:offset="1.0" />
            </gradient>
        </aapt:attr>
    </path>
    
    <!-- Top Glass Gloss Highlight -->
    <path android:pathData="M100,14 c-42,0 -75,18 -84,46 c18,-24 48,-36 84,-36 c36,0 66,12 84,36 c-9,-28 -42,-46 -84,-46 z">
        <aapt:attr name="android:fillColor">
            <gradient android:endY="60" android:startY="14" android:type="linear" android:startX="100" android:endX="100">
                <item android:color="#B3FFFFFF" android:offset="0" />
                <item android:color="#00FFFFFF" android:offset="1" />
            </gradient>
        </aapt:attr>
    </path>
"""

emojis = {
    "rate_0": f"""
    <!-- Eyebrows (Shocked) -->
    <path android:pathData="M 45,55 Q 65,40 85,55" android:strokeColor="#3E2723" android:strokeWidth="7" android:strokeLineCap="round" />
    <path android:pathData="M 115,55 Q 135,40 155,55" android:strokeColor="#3E2723" android:strokeWidth="7" android:strokeLineCap="round" />
    
    <!-- Wide Shocked Eyes -->
    {circle_path(65, 80, 14, "#3E2723")}
    {circle_path(62, 76, 5, "#FFFFFF")}
    {circle_path(135, 80, 14, "#3E2723")}
    {circle_path(132, 76, 5, "#FFFFFF")}
    
    <!-- Open Shocked Mouth -->
    <path android:pathData="M100,122 m-16,0 a16,20 0 1,1 32,0 a16,20 0 1,1 -32,0" android:fillColor="#3E2723" />
    <path android:pathData="M100,132 m-10,0 a10,8 0 1,1 20,0 a10,8 0 1,1 -20,0" android:fillColor="#FF5252" />
    </vector>""",
    
    "rate_1": """
    <!-- Sad Eyes -->
    <path android:pathData="M 45,72 Q 65,52 85,72" android:strokeColor="#3E2723" android:strokeWidth="9" android:strokeLineCap="round"/>
    <path android:pathData="M 115,72 Q 135,52 155,72" android:strokeColor="#3E2723" android:strokeWidth="9" android:strokeLineCap="round"/>
    
    <!-- Shiny Tear Drops -->
    <path android:pathData="M 52,85 C 42,95 42,112 55,112 C 68,112 68,95 58,85 Z" android:fillColor="#38BDF8" />
    <path android:pathData="M 148,85 C 138,95 138,112 151,112 C 164,112 164,95 154,85 Z" android:fillColor="#38BDF8" />
    
    <!-- Sad Mouth -->
    <path android:pathData="M 65,148 Q 100,120 135,148" android:strokeColor="#3E2723" android:strokeWidth="10" android:strokeLineCap="round"/>
    </vector>""",
    
    "rate_2": f"""
    <!-- Disappointed Eyebrows -->
    <path android:pathData="M 45,55 L 85,70" android:strokeColor="#3E2723" android:strokeWidth="8" android:strokeLineCap="round"/>
    <path android:pathData="M 155,55 L 115,70" android:strokeColor="#3E2723" android:strokeWidth="8" android:strokeLineCap="round"/>
    
    <!-- Disappointed Eyes -->
    {circle_path(65, 85, 10, "#3E2723")}
    {circle_path(135, 85, 10, "#3E2723")}
    
    <!-- Crooked/Wavy Discontent Mouth -->
    <path android:pathData="M 68,142 Q 95,128 132,138" android:strokeColor="#3E2723" android:strokeWidth="10" android:strokeLineCap="round"/>
    </vector>""",
    
    "rate_3": f"""
    <!-- Neutral Eyes -->
    {circle_path(65, 78, 11, "#3E2723")}
    {circle_path(62, 74, 4, "#FFFFFF")}
    {circle_path(135, 78, 11, "#3E2723")}
    {circle_path(132, 74, 4, "#FFFFFF")}
    
    <!-- Rosy Cheek Blush -->
    {circle_path(48, 100, 12, "#20FF5252")}
    {circle_path(152, 100, 12, "#20FF5252")}
    
    <!-- Straight Neutral Mouth -->
    <path android:pathData="M 70,135 L 130,135" android:strokeColor="#3E2723" android:strokeWidth="10" android:strokeLineCap="round"/>
    </vector>""",
    
    "rate_4": f"""
    <!-- Happy Arc Eyes -->
    <path android:pathData="M 48,78 Q 65,56 82,78" android:strokeColor="#3E2723" android:strokeWidth="9" android:strokeLineCap="round"/>
    <path android:pathData="M 118,78 Q 135,56 152,78" android:strokeColor="#3E2723" android:strokeWidth="9" android:strokeLineCap="round"/>
    
    <!-- Rosy Cheeks -->
    {circle_path(45, 100, 14, "#35FF5252")}
    {circle_path(155, 100, 14, "#35FF5252")}
    
    <!-- Big Smile with Tongue -->
    <path android:pathData="M 55,115 C 55,160 145,160 145,115 Z" android:fillColor="#3E2723" />
    <path android:pathData="M 75,135 C 75,125 125,125 125,135 C 125,156 75,156 75,135 Z" android:fillColor="#FF5252" />
    </vector>""",
    
    "rate_5": f"""
    <!-- 3D Shiny Heart Eyes -->
    <path android:pathData="M 65,45 C 45,45 40,70 65,92 C 90,70 85,45 65,45 Z" android:fillColor="#FF2D55" />
    <path android:pathData="M 60,50 C 50,50 48,60 60,72 C 60,60 55,50 60,50 Z" android:fillColor="#FFFFCC" />
    
    <path android:pathData="M 135,45 C 115,45 110,70 135,92 C 160,70 155,45 135,45 Z" android:fillColor="#FF2D55" />
    <path android:pathData="M 130,50 C 120,50 118,60 130,72 C 130,60 125,50 130,50 Z" android:fillColor="#FFFFCC" />
    
    <!-- Rosy Cheeks -->
    {circle_path(42, 105, 15, "#40FF2D55")}
    {circle_path(158, 105, 15, "#40FF2D55")}
    
    <!-- Joyful Open Smile with Tongue -->
    <path android:pathData="M 50,115 C 50,168 150,168 150,115 Z" android:fillColor="#3E2723" />
    <path android:pathData="M 70,138 C 70,126 130,126 130,138 C 130,162 70,162 70,138 Z" android:fillColor="#FF4081" />
    </vector>"""
}

# Write 3D Emojis
for name, content in emojis.items():
    write_file(os.path.join(drawable_dir, f"{name}.xml"), emoji_base + content)

# Cute Puffy 3D Claymorphism Golden Star (Filled) - Exactly Matching User Image
star_filled = """<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:aapt="http://schemas.android.com/aapt"
    android:width="100dp"
    android:height="100dp"
    android:viewportWidth="100"
    android:viewportHeight="100">

    <!-- Soft Golden Ambient Drop Shadow -->
    <path
        android:pathData="M 50,12 Q 54,12 58,23 Q 62,35 72,35 Q 82,35 89,39 Q 94,42 90,52 Q 85,62 87,72 Q 89,82 80,88 Q 75,91 66,86 Q 57,81 50,81 Q 43,81 34,86 Q 25,91 20,88 Q 11,82 13,72 Q 15,62 10,52 Q 6,42 11,39 Q 18,35 28,35 Q 38,35 42,23 Q 46,12 50,12 Z"
        android:fillColor="#35FF8F00" />

    <!-- Plump Puffy 3D Claymorphism Golden Star Body -->
    <path android:pathData="M 50,8 Q 54,8 58,19 Q 62,31 72,31 Q 82,31 89,35 Q 94,38 90,48 Q 85,58 87,68 Q 89,78 80,84 Q 75,87 66,82 Q 57,77 50,77 Q 43,77 34,82 Q 25,87 20,84 Q 11,78 13,68 Q 15,58 10,48 Q 6,38 11,35 Q 18,31 28,31 Q 38,31 42,19 Q 46,8 50,8 Z">
        <aapt:attr name="android:fillColor">
            <gradient
                android:type="radial"
                android:centerX="42"
                android:centerY="30"
                android:gradientRadius="72">
                <item android:color="#FFFFFCF5" android:offset="0.0" />
                <item android:color="#FFFFD54F" android:offset="0.25" />
                <item android:color="#FFFFB300" android:offset="0.65" />
                <item android:color="#FFFF8F00" android:offset="1.0" />
            </gradient>
        </aapt:attr>
    </path>

    <!-- Top Cushion Specular Highlight Arc -->
    <path
        android:pathData="M 50,8 Q 54,8 58,19 Q 62,31 72,31 Q 82,31 89,35 C 79,25 61,23 50,23 C 39,23 21,25 11,35 Q 18,31 28,31 Q 38,31 42,19 Q 46,8 50,8 Z"
        android:fillColor="#65FFFFFF" />

    <!-- Delicate Warm Light Golden Inner Rim -->
    <path
        android:pathData="M 50,8 Q 54,8 58,19 Q 62,31 72,31 Q 82,31 89,35 Q 94,38 90,48 Q 85,58 87,68 Q 89,78 80,84 Q 75,87 66,82 Q 57,77 50,77 Q 43,77 34,82 Q 25,87 20,84 Q 11,78 13,68 Q 15,58 10,48 Q 6,38 11,35 Q 18,31 28,31 Q 38,31 42,19 Q 46,8 50,8 Z"
        android:strokeWidth="1.2"
        android:strokeColor="#FFE082" />
</vector>
"""
write_file(os.path.join(drawable_dir, "rate_star_filled.xml"), star_filled)

# Matching Plump Puffy Empty Star (Soft Light Slate)
star_empty = """<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="100dp"
    android:height="100dp"
    android:viewportWidth="100"
    android:viewportHeight="100">

    <!-- Soft Light Pastel Slate Fill -->
    <path
        android:pathData="M 50,8 Q 54,8 58,19 Q 62,31 72,31 Q 82,31 89,35 Q 94,38 90,48 Q 85,58 87,68 Q 89,78 80,84 Q 75,87 66,82 Q 57,77 50,77 Q 43,77 34,82 Q 25,87 20,84 Q 11,78 13,68 Q 15,58 10,48 Q 6,38 11,35 Q 18,31 28,31 Q 38,31 42,19 Q 46,8 50,8 Z"
        android:fillColor="#F1F5F9" />

    <!-- Crisp Soft Slate Border -->
    <path
        android:pathData="M 50,8 Q 54,8 58,19 Q 62,31 72,31 Q 82,31 89,35 Q 94,38 90,48 Q 85,58 87,68 Q 89,78 80,84 Q 75,87 66,82 Q 57,77 50,77 Q 43,77 34,82 Q 25,87 20,84 Q 11,78 13,68 Q 15,58 10,48 Q 6,38 11,35 Q 18,31 28,31 Q 38,31 42,19 Q 46,8 50,8 Z"
        android:strokeWidth="2.2"
        android:strokeColor="#CBD5E1"
        android:strokeLineJoin="round"
        android:strokeLineCap="round" />
</vector>
"""
write_file(os.path.join(drawable_dir, "rate_star_empty.xml"), star_empty)

# Premium Wavy Header Background
wave_header = """<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:aapt="http://schemas.android.com/aapt"
    android:width="400dp"
    android:height="120dp"
    android:viewportWidth="400"
    android:viewportHeight="120">

    <!-- Base Gradient Background Layer -->
    <path android:pathData="M0,0 L400,0 L400,120 L0,120 Z">
        <aapt:attr name="android:fillColor">
            <gradient
                android:type="linear"
                android:startX="0"
                android:startY="0"
                android:endX="400"
                android:endY="120">
                <item android:color="#FFEBF3FF" android:offset="0.0" />
                <item android:color="#FFE0ECFF" android:offset="0.5" />
                <item android:color="#FFD6E6FE" android:offset="1.0" />
            </gradient>
        </aapt:attr>
    </path>

    <!-- BACK WAVE LAYER -->
    <path android:pathData="M0,0 L400,0 L400,75 C310,110 210,50 110,80 C60,95 25,108 0,120 Z">
        <aapt:attr name="android:fillColor">
            <gradient
                android:type="linear"
                android:startX="0"
                android:startY="0"
                android:endX="400"
                android:endY="100">
                <item android:color="#FFC7E0FF" android:offset="0.0" />
                <item android:color="#FF99C8FF" android:offset="1.0" />
            </gradient>
        </aapt:attr>
    </path>

    <!-- FRONT GLOSSY WAVE LAYER -->
    <path android:pathData="M0,0 L400,0 L400,55 C300,35 190,95 90,80 C45,72 20,55 0,40 Z">
        <aapt:attr name="android:fillColor">
            <gradient
                android:type="linear"
                android:startX="0"
                android:startY="0"
                android:endX="350"
                android:endY="80">
                <item android:color="#FFF8FBFF" android:offset="0.0" />
                <item android:color="#FFBAE0FF" android:offset="1.0" />
            </gradient>
        </aapt:attr>
    </path>

    <!-- HIGHLIGHT CURVE -->
    <path
        android:pathData="M0,40 C20,55 45,72 90,80 C190,95 300,35 400,55"
        android:strokeWidth="1.5"
        android:strokeColor="#80FFFFFF"
        android:strokeLineCap="round" />
</vector>
"""
write_file(os.path.join(drawable_dir, "rate_wave_header.xml"), wave_header)

# Vibrant 3D Pill Button (Rate Button)
btn_rate = """<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- Bottom 3D Bevel / Shadow Layer -->
    <item android:top="3dp">
        <shape android:shape="rectangle">
            <corners android:radius="24dp"/>
            <solid android:color="#D83050"/>
        </shape>
    </item>
    <!-- Main Gradient Body -->
    <item android:bottom="3dp">
        <shape android:shape="rectangle">
            <corners android:radius="24dp"/>
            <gradient
                android:startColor="#FF7356"
                android:endColor="#FF3E6C"
                android:angle="0"/>
        </shape>
    </item>
    <!-- Top Inner Specular Highlight -->
    <item android:bottom="3dp" android:top="1dp" android:left="3dp" android:right="3dp">
        <shape android:shape="rectangle">
            <corners android:radius="24dp"/>
            <stroke android:width="1dp" android:color="#40FFFFFF"/>
        </shape>
    </item>
</layer-list>
"""
write_file(os.path.join(drawable_dir, "rate_bg_button.xml"), btn_rate)

# Modern Card Background (dialog body)
card_bg = """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <corners android:radius="20dp" />
    <solid android:color="#FFFFFF" />
    <stroke android:width="1dp" android:color="#F1F5F9" />
</shape>
"""
write_file(os.path.join(drawable_dir, "rate_rounded_rectangle.xml"), card_bg)

# Cancel Button Background
btn_cancel = """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <corners android:radius="20dp" />
    <solid android:color="#F1F5F9" />
</shape>
"""
write_file(os.path.join(drawable_dir, "rate_bg_button_cancel.xml"), btn_cancel)

# Send Button Background
btn_send = """<?xml version="1.0" encoding="utf-8"?>
<shape android:shape="rectangle" xmlns:android="http://schemas.android.com/apk/res/android">
    <corners android:radius="20dp" />
    <gradient
        android:startColor="#10B981"
        android:endColor="#059669"
        android:angle="0"/>
</shape>
"""
write_file(os.path.join(drawable_dir, "rate_bg_button_send.xml"), btn_send)

print("Generated Puffy 3D Claymorphism Golden Stars matching user image perfectly!")
