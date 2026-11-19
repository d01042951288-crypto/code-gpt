import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="나만의 학습게임 기획하기", page_icon="🎮", layout="wide")

# 화사하고 개성 있는 컬러 테마
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');

:root {
  --ink: #26324b;
  --muted: #68738a;
  --pink: #ff6f91;
  --purple: #8067f7;
  --blue: #55b8f5;
  --yellow: #ffd166;
  --mint: #63d8bd;
}
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
.stApp {
  background:
    radial-gradient(circle at 8% 5%, rgba(255, 194, 213, .42), transparent 25%),
    radial-gradient(circle at 94% 12%, rgba(168, 218, 255, .48), transparent 27%),
    radial-gradient(circle at 80% 92%, rgba(193, 245, 222, .45), transparent 28%),
    linear-gradient(135deg, #fff9f2 0%, #f7f5ff 48%, #f1fbff 100%);
  color: var(--ink);
}
.block-container { max-width: 1180px; padding-top: 2.1rem; padding-bottom: 4rem; }
.hero {
  position: relative; overflow: hidden; padding: 30px 32px; margin-bottom: 26px;
  border-radius: 26px; color: white;
  background: linear-gradient(115deg, #7657e8 0%, #a56cf0 42%, #ff8eaa 100%);
  box-shadow: 0 14px 34px rgba(119, 89, 220, .22);
}
.hero:after { content: "✦  ✧  ✦"; position:absolute; right:24px; top:16px;
  font-size:30px; letter-spacing:12px; opacity:.55; }
.hero h1 { font-family:'Jua',sans-serif; font-size:2.35rem; margin:0 0 8px; color:white; }
.hero p { margin:0; font-size:1rem; opacity:.94; }
.step-header {
  color: #293451; font-family:'Jua',sans-serif; font-weight:700; font-size:1.55rem;
  margin-top: 1.8rem; margin-bottom: .85rem; display:flex; align-items:center; gap:12px;
}
.badge {
  background: linear-gradient(120deg, #ff7298, #ffad78); color:white;
  padding:7px 15px; border-radius:999px; font-size:.82rem; font-weight:800;
  letter-spacing:.4px; box-shadow:0 5px 12px rgba(255,114,152,.2);
}
.recommend-box {
  background:linear-gradient(145deg, #e7fff7, #f0faff);
  border:1px solid #b8efdf; border-radius:20px; padding:20px;
  box-shadow:0 8px 22px rgba(73,173,153,.10); height:100%;
}
.guide-box {
  background:rgba(255,255,255,.88); border:1px solid #e6e4f7;
  border-radius:17px; padding:19px; margin-bottom:10px;
  box-shadow:0 7px 18px rgba(71,78,130,.07); transition:transform .2s ease;
}
.guide-box:hover { transform:translateY(-3px); }
.stRadio [role=radiogroup] { flex-wrap:wrap; gap:9px; }
.stRadio [role=radio] {
  background:rgba(255,255,255,.82); border:1px solid #e6e1fb;
  border-radius:13px; padding:8px 12px; min-height:42px;
}
.stTextInput input, .stTextArea textarea {
  background:rgba(255,255,255,.92)!important; border:1.5px solid #e3def8!important;
  border-radius:13px!important; color:#26324b!important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
  border-color:#9278f5!important; box-shadow:0 0 0 3px rgba(146,120,245,.13)!important;
}
.stButton > button {
  border:0; border-radius:14px; color:white; font-weight:800;
  background:linear-gradient(100deg,#7961ed,#ee78a4);
  box-shadow:0 7px 16px rgba(126,96,222,.2); padding:.72rem 1rem;
  transition:transform .18s ease, box-shadow .18s ease;
}
.stButton > button:hover { color:white; transform:translateY(-2px); box-shadow:0 10px 20px rgba(126,96,222,.27); }
.stAlert { border-radius:14px; }
div[data-testid="stCode"] {
  border:1px solid #e4defa; border-radius:16px; overflow:hidden;
  box-shadow:0 8px 22px rgba(71,78,130,.07);
}
hr { border-color:rgba(137,122,198,.18); margin:2rem 0; }
.stCaption { color:var(--muted); }
@media(max-width:640px) {
  .block-container { padding:1rem 1rem 3rem; }
  .hero { padding:24px 20px; border-radius:20px; }
  .hero h1 { font-size:1.8rem; }
  .step-header { font-size:1.3rem; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>🎨 나만의 학습게임 스튜디오</h1>
  <p>상상한 아이디어를 고르고 적으면, AI가 플레이할 수 있는 학습게임으로 만들어줘요!</p>
</div>
""", unsafe_allow_html=True)

# --- STEP 1 ---
st.markdown('<div class="step-header"><span class="badge">STEP 1</span> 나만의 게임 기획하기</div>', unsafe_allow_html=True)
st.caption("✨ 게임의 종류와 학습 내용을 정하고, 나만의 아이디어를 자유롭게 꾸며보세요.")

col1, col2 = st.columns([2, 1])

with col1:
    game_type = st.radio(
        "게임 종류", 
        ["📝 퀴즈", "⚔️ 액션", "🎲 보드", "🗺️ 어드벤처", "🧩 퍼즐", "⌨️ 타이핑", "⏱️ 타이머 경쟁", "🚪 방탈출"], 
        horizontal=True
    )
    
    grade = st.radio(
        "학년 수준", 
        ["1학년", "2학년", "3학년", "4학년", "5학년", "6학년"], 
        index=5, 
        horizontal=True
    )
    
    # value 속성을 placeholder로 변경하여 흐린 글씨로 나타나도록 수정
    title_input = st.text_input("게임 제목", placeholder="예: 역사 히어로즈 대작전")
    topic_input = st.text_area("학습 주제", placeholder="예: 우리나라 역사 인물 알아보기 (단군왕검, 세종대왕, 이순신 등)")
    rules_input = st.text_area("게임 규칙 및 방법", placeholder="예: 각 스테이지마다 역사 인물에 대한 퀴즈가 나오고, 맞히면 다음 단계로 넘어감. 틀리면 목숨이 줄어듦. 총 3번 틀리면 게임 오버.")
    design_input = st.text_input("디자인 스타일", placeholder="예: 레트로 픽셀 아트 스타일, 배경음악은 웅장하게")
    
    # 사용자가 아무것도 입력하지 않았을 때 들어갈 기본값(프롬프트용)
    title = title_input if title_input else "[제목을 입력해주세요]"
    topic = topic_input if topic_input else "[주제를 입력해주세요]"
    rules = rules_input if rules_input else "[게임 규칙을 입력해주세요]"
    design = design_input if design_input else "[디자인 스타일을 입력해주세요]"

with col2:
    st.markdown(f'''
    <div class="recommend-box">
        <h4 style="color: #0c6b58; margin-top: 0;">{grade} 추천 학습 주제</h4>
        <p style="font-size: 0.9rem; color: #444;">스스로 학습 주제를 정하기 어렵다면 활용해보세요.</p>
        <div style="background: white; padding: 10px; border-radius: 8px; border: 1px solid #ccc; margin-bottom: 10px;">
            <strong>국어:</strong> 우리말의 구조와 쓰임
        </div>
        <div style="background: white; padding: 10px; border-radius: 8px; border: 1px solid #ccc; margin-bottom: 10px;">
            <strong>과학:</strong> 우리 몸의 구조와 기능
        </div>
        <div style="background: white; padding: 10px; border-radius: 8px; border: 1px solid #ccc; margin-bottom: 10px;">
            <strong>역사:</strong> 조선시대의 문화와 과학 발전
        </div>
        <p style="font-size: 0.8rem; color: #666; margin-top: 15px;">
            💡 작성하신 내용, 특히, 칸에 쓰인 모든 의견장에는 추천 정보입니다.
        </p>
    </div>
    ''', unsafe_allow_html=True)


# --- STEP 2 ---
st.markdown("---")
st.markdown('<div class="step-header"><span class="badge">STEP 2</span> 게임 제작 프롬프트 복사하기</div>', unsafe_allow_html=True)
st.caption("🚀 작성한 기획이 AI에게 전달할 수 있는 게임 제작 프롬프트로 바뀌었어요!")

# 프롬프트 생성
clean_game_type = game_type.split(" ")[1] # 이모지 제거

prompt_text = f'''너는 훌륭하고 실력 있는 게임 개발 프로그래머야. 초등학생 {grade} 수준에 맞게 좋아하는 요소들과 학습을 결합해 즐길 수 있는 재미있는 웹 기반 게임을 만들어야 해. HTML, CSS, JavaScript 코드를 합쳐서 하나의 HTML 파일 코드로 결과를 완성해서 보여줘.

[게임 기획]
- 게임 제목: {title}
- 학습 주제: {topic}
- 게임 규칙 및 방법: {rules}
- 디자인 스타일: {design}
- 게임 종류: {clean_game_type}
- 학년 수준: 초등학생 {grade} (이 수준의 학생이 이해하고 즐길 수 있도록 만들어 줘)

[코드 작성 시 필수 조건]
- 코드는 반드시 분리하지 말고 하나의 index.html 파일 안에 HTML, CSS, JS가 모두 포함되도록 작성해 줘.

[세부 개발 조건]
1. 모바일 기기에서도 화면이 깨지지 않고 잘 보이도록 반응형으로 만들어 줘.
2. 게임 시작 전 타이틀 화면이 있어야 하며, '게임 시작' 버튼을 만들어 줘.
3. 점수나 남은 시간, 목숨 등을 화면 상단에 잘 보이게 표시해 줘.
4. 정답을 맞추거나 틀렸을 때 시각적인 효과나 색상 변화를 줘서 바로 알 수 있게 해 줘.
5. 게임이 끝나면 최종 점수와 함께 '다시 하기' 버튼이 나타나게 해 줘.
6. 디자인은 제시한 스타일에 맞게 최대한 예쁘고 가독성 좋게 꾸며 줘.
7. 필요한 이미지가 있다면 CSS 속성을 이용해 직접 그리거나 이모지를 활용해 줘.
8. 배경색, 글꼴색 등은 눈이 편안한 색상 조합을 사용해 줘.
9. 코드 실행은 간단하게 구동 가능하며, 실행 가능한 전체 코드를 코드 블록에 넣어 줘.
'''

st.info("💡 아래 코드 박스 우측 상단의 📋 버튼을 누르면 프롬프트가 복사됩니다.")
st.code(prompt_text, language="markdown")

if st.button("🌟 제미나이(Gemini) 열기", use_container_width=True):
    st.markdown('<meta http-equiv="refresh" content="0; url=https://gemini.google.com/">', unsafe_allow_html=True)


# --- STEP 3 ---
st.markdown("---")
st.markdown('<div class="step-header"><span class="badge">STEP 3</span> 게임 제작 방법 안내</div>', unsafe_allow_html=True)

st.markdown('''
<div style="display: flex; gap: 15px; flex-wrap: wrap;">
    <div class="guide-box" style="flex: 1; min-width: 200px;">
        <h4 style="color: #8067f7;">🌈 STEP 1</h4>
        <p>만들고 싶은 게임을 기획한다.</p>
    </div>
    <div class="guide-box" style="flex: 1; min-width: 200px;">
        <h4 style="color: #ff7298;">🧩 STEP 2</h4>
        <p>게임 제목, 규칙/방법 내용, 규칙, 디자인을 정한다.</p>
    </div>
    <div class="guide-box" style="flex: 1; min-width: 200px;">
        <h4 style="color: #20a98e;">🤖 STEP 3</h4>
        <p>작성된 제작 프롬프트를 복사하여 AI(제미나이 등)에게 명령을 내린다.</p>
    </div>
    <div class="guide-box" style="flex: 1; min-width: 200px;">
        <h4 style="color: #e39b24;">🎉 STEP 4</h4>
        <p>제미나이가 만들어준 코드를 복사해서 HTML 파일을 만들어 확인하고 수정한다.</p>
    </div>
</div>

<div class="recommend-box" style="background-color: #fff3cd; border-color: #ffe69c; margin-top: 20px;">
    <h4 style="color: #856404; margin-top: 0;">💡 제미나이가 만든 코드로 게임 실행하기</h4>
    <ol style="color: #533f03; line-height: 1.8;">
        <li>제미나이가 만든 HTML 코드를 우측 상단의 <strong>복사 버튼</strong>을 눌러 복사합니다.</li>
        <li>컴퓨터(PC) 바탕화면에서 마우스 우클릭 후 <strong>새로 만들기 > 텍스트 문서</strong>를 선택합니다.</li>
        <li>텍스트 문서(메모장)를 열고 복사한 코드를 <strong>붙여넣기(Ctrl+V)</strong> 합니다.</li>
        <li>상단 메뉴에서 <strong>파일 > 다른 이름으로 저장</strong>을 클릭합니다.</li>
        <li>파일 이름을 <code>game.html</code>로 적고, 파일 형식은 '모든 파일'로 변경 후 저장합니다.</li>
        <li>저장된 <code>game.html</code> 파일을 더블클릭하면 웹 브라우저에서 나만의 게임이 실행됩니다!</li>
    </ol>
</div>
''', unsafe_allow_html=True)
