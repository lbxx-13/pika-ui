[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · 한국어 · [Deutsch](README.de.md) · [Español](README.es.md)

<p align="center">
  <img src="assets/pika-ui-logo.png" width="300" alt="Pika UI 컬러 픽업트럭 로고">
</p>

<h1 align="center">Pika UI</h1>

<p align="center"><strong>실제 과제에서 시작해 UI를 명확하게 설계하고, 프로젝트에 맞는 기술로 구현합니다.</strong></p>

Pika UI는 AI 코딩 에이전트를 위한 크로스 플랫폼 UI 설계 및 구현 스킬입니다. 웹, 데스크톱, 모바일을 비롯한 다양한 소프트웨어 화면에서 새 UI 제작, 리디자인, 스크린샷 재현, UI 리뷰를 지원합니다.

React Bits는 선택적으로 참고할 수 있는 시각 및 인터랙션 자료이며, 특정 기술 스택을 요구하지 않습니다. React 프로젝트에서는 필요할 때 컴포넌트를 검토하고, 다른 스택에서는 효과를 대상 플랫폼에 맞게 구현합니다.

## 설치

### 터미널에서 설치

어느 디렉터리에서든 아래 명령을 실행하세요. 선택한 AI 코딩 에이전트에 `pika-ui` 스킬만 전역 설치합니다.

```bash
npx skills add lbxx-13/pika-ui --skill pika-ui -g
```

이 GitHub 저장소는 현재 비공개입니다. 명령을 실행하는 컴퓨터에 Git 자격 증명, GitHub CLI 로그인 또는 SSH를 통한 저장소 접근 권한이 있어야 합니다. 선택 화면이 나타나면 사용할 에이전트를 고르세요. 여러 에이전트를 지정하려면 `-a` 옵션을 추가하세요(예: `-a codex -a claude-code -a cursor`).

### 에이전트에게 설치 요청

터미널 명령을 실행할 수 있는 AI 코딩 에이전트에 다음 문장을 보내세요.

```text
현재 AI 코딩 에이전트에 Pika UI 스킬을 설치해 주세요. 다음 명령을 실행하세요: npx skills add lbxx-13/pika-ui --skill pika-ui -g
```

에이전트를 실행하는 컴퓨터에도 이 비공개 GitHub 저장소에 접근할 권한이 필요합니다. 인증 오류가 발생하면 GitHub 접근을 설정한 뒤 명령을 다시 실행하세요.

### 나중에 업데이트

```bash
npx skills update pika-ui -g
```

Codex에 저장소를 직접 clone해 설치했다면 다음 명령으로 업데이트하세요.

```bash
git -C ~/.codex/skills/pika-ui pull --ff-only
```

사용자 지정 `CODEX_HOME`을 사용한다면 `~/.codex`를 Codex 홈 디렉터리로 바꾸세요.

## Pika UI 사용법

설치한 뒤 필요하면 에이전트를 다시 시작하거나 새로고침하세요. 스킬을 이름으로 직접 호출하는 기능이 있으면 사용하고, 없으면 “Pika UI 스킬을 사용해 주세요”라고 요청하세요. 관련 프로젝트, 스크린샷, 브랜드 자료와 제약 조건을 제공하면 기존 기술 스택을 확인하고 필요한 가이드만 읽습니다.

## 할 수 있는 작업

- **새 UI 설계:** 제품 페이지, 작업 공간, 모바일 화면 또는 컴포넌트의 방향을 정하고 구현합니다.
- **기존 UI 개선:** 프로젝트의 페이지, 디자인 토큰, 공유 컴포넌트와 동작을 파악한 뒤 변경합니다.
- **참고 이미지 재현:** 레이아웃, 비율, 글꼴, 색상, 계층을 재현하고 목표 뷰포트에서 확인합니다.
- **디자인 방향 비교:** 요청에 따라 실질적으로 다른 최대 3개 안을 만들고 로컬 비교 페이지에서 나란히 살펴봅니다.
- **사용 경험 리뷰:** 계층, 반응형 레이아웃, 인터랙션 상태, 키보드 접근성 및 모션 감소 동작을 확인합니다.
- **모션과 미디어 탐색:** React Bits를 선택적 컴포넌트 참고로 활용하거나 이미지, 아이콘, 모션을 고릅니다.

## 프롬프트 예시

```text
Pika UI를 사용해 이 강의 예약 서비스의 랜딩 페이지를 미리 볼 수 있도록 만들어 주세요. 대상 사용자와 강의 콘텐츠를 바탕으로 방향을 정하고 데스크톱과 모바일 레이아웃을 구현해 주세요.
```

```text
Pika UI를 사용해 이 스크린샷을 재현해 주세요. 먼저 프로젝트의 프레임워크와 스타일 규칙을 확인하고, 구현 후 좁은 화면 레이아웃도 살펴봐 주세요.
```

```text
Pika UI로 이 페이지를 리뷰해 주세요. 스크린샷이나 코드 근거가 있는 문제와 구체적인 수정 제안만 보고하고 파일은 변경하지 마세요.
```

## 작업 흐름

1. **맥락 파악:** 대상 사용자, 주요 과제, 기기, 기존 UI와 프로젝트 기술 스택을 확인합니다.
2. **디자인 결정:** 핵심 초점, 주요 동작, 시각 방향, 글꼴과 색상, 주요 이미지 및 상태를 정합니다.
3. **프로젝트에 맞게 구현:** 기존 컴포넌트, 디자인 토큰, 의존성 및 플랫폼 관례를 따릅니다.
4. **실제 UI 확인:** 목표 뷰포트, 주요 상태와 동작을 살펴보고 불필요한 세부 요소를 정리합니다.

참고 문서는 작업에 필요한 항목만 읽습니다. 작고 명확한 수정은 전체 방향 설정 절차 없이 바로 진행할 수 있습니다.

## 가이드 맵

| 작업 | 가이드 |
| --- | --- |
| 새 UI, 리디자인 및 구현 | [`references/design-workflow.md`](references/design-workflow.md) |
| 시각 방향 및 콘셉트 탐색 | [`references/design-direction.md`](references/design-direction.md), [`references/task-explore.md`](references/task-explore.md) |
| 마케팅, 브랜드 및 출시 페이지 | [`references/direction-persuasion.md`](references/direction-persuasion.md) |
| 스크린샷 재현, 레이아웃 및 뷰포트 | [`references/layout-and-viewport.md`](references/layout-and-viewport.md) |
| 글꼴, 색상, 표면 및 계층 | [`references/visual-language.md`](references/visual-language.md) |
| 디자인 토큰과 시스템 관리 | [`references/design-system.md`](references/design-system.md) |
| 폼, 다이얼로그 및 복잡한 상태 | [`references/interaction-states.md`](references/interaction-states.md) |
| 모션과 모션 감소 설정 | [`references/motion.md`](references/motion.md) |
| 이미지, 아이콘 및 미디어 출처 | [`references/media.md`](references/media.md) |
| UX 흐름 점검 | [`references/ux-review.md`](references/ux-review.md) |
| 읽기 전용 UI 리뷰 | [`references/task-review.md`](references/task-review.md), [`references/review-checklist.md`](references/review-checklist.md) |
| 후보안 비교 | [`references/style-explorer.md`](references/style-explorer.md) |
| 브라우저 및 개발 도구 | [`references/tools.md`](references/tools.md) |

### React Bits의 역할

[React Bits](https://reactbits.dev/)는 텍스트 애니메이션, 배경, 컴포넌트, 마이크로 인터랙션 예제를 제공합니다. Pika UI에서는 시각 및 인터랙션 아이디어를 위한 선택적 참고 자료로 사용합니다. 참고하거나 적용하기 전에 [`references/react-bits.md`](references/react-bits.md)를 확인하세요. React 소스 컴포넌트는 대상 프로젝트가 React를 사용하고 적합한 경우에만 직접 통합하고, 다른 플랫폼에서는 의도와 시각 효과를 해당 환경에 맞게 구현합니다.

## 저장소 구조

```text
SKILL.md                          스킬 진입점과 작업 라우팅
references/                       설계, 구현, 리뷰 가이드
assets/style-explorer.html        로컬 후보 비교 페이지
assets/pika-ui-logo.png           Pika UI 픽업트럭 로고
scripts/create_style_explorer.py  비교 페이지 링크 생성 스크립트
```

비교 페이지는 이미 만들어진 후보를 보는 도구입니다. 디자인 방향을 대신 탐색하거나 자동으로 생성하지 않습니다.

## 설계 원칙

- 고정된 스타일을 강요하지 않고 프로젝트의 브랜드, 기술 스택, 컴포넌트와 플랫폼 관례를 따릅니다.
- 프로젝트에서 제공되거나 검증된 사실만 사용하고 지표, 고객 후기, 기능 약속을 지어내지 않습니다.
- React Bits는 크로스 플랫폼 컴포넌트 라이브러리나 유일한 컴포넌트 출처가 아닙니다. 아이디어를 대상 스택에 맞게 적용합니다.
- 시각 디자인, 인터랙션, 기능을 따로 확인합니다. 실제 실행하지 않은 부분은 미검증으로 표시합니다.

