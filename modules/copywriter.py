from dataclasses import dataclass

@dataclass
class CopyRequest:
    product: str
    scene: str
    audience: str
    goal: str
    tone: str = "清晰、有吸引力"

def generate_copy(req: CopyRequest) -> dict:
    """Generate deterministic starter copy without requiring an external API."""
    product = req.product.strip() or "产品"
    scene = req.scene.strip() or "社交媒体"
    audience = req.audience.strip() or "目标用户"
    goal = req.goal.strip() or "提升关注"

    templates = {
        "种草": (
            f"{product}，给{audience}一个更轻松的{goal}思路",
            f"{scene}｜把复杂的选择变简单，先从适合自己的方案开始。",
            "亮点\n• 信息清晰\n• 场景明确\n• 便于快速理解",
        ),
        "转化": (
            f"{product}｜现在开始，为{goal}做准备",
            f"{scene}｜突出核心卖点，减少无关信息，让用户更快找到重点。",
            "行动建议\n• 明确核心利益点\n• 给出使用场景\n• 保留清晰行动入口",
        ),
        "品牌": (
            f"{product}｜让每一次选择都有理由",
            f"{scene}｜用简洁、有辨识度的表达建立稳定的品牌记忆。",
            "表达方向\n• 统一品牌语气\n• 突出差异化\n• 保持视觉与文案一致",
        ),
    }

    key = next((k for k in templates if k in req.goal), "种草")
    title, subtitle, body = templates[key]
    return {"title": title, "subtitle": subtitle, "body": body, "audience": audience}
