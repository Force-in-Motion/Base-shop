"""create table Profile and add field created_at by table Post

Revision ID: 51b0931394cd
Revises: 874c0eb106b1
Create Date: 2025-07-22 15:11:51.947919

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "51b0931394cd"
down_revision: Union[str, Sequence[str], None] = "874c0eb106b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "Profile",
        sa.Column("floor", sa.String(), nullable=True),
        sa.Column("age", sa.Integer(), nullable=True),
        sa.Column("married", sa.Boolean(), nullable=True),
        sa.Column("bio", sa.String(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["User.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column(
        "Post",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.add_column(
        "User", sa.Column("address", sa.String(length=150), nullable=False)
    )
    op.drop_column("User", "age")
    op.drop_column("User", "floor")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "User",
        sa.Column("floor", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "User",
        sa.Column("age", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_column("User", "address")
    op.drop_column("Post", "created_at")
    op.drop_table("Profile")
    # ### end Alembic commands ###
