-- CreateEnum
CREATE TYPE "AccountRole" AS ENUM ('USER', 'ADMIN', 'BOT');

-- CreateEnum
CREATE TYPE "gameType" AS ENUM ('LPVP', 'OPVP', 'PVB');

-- CreateEnum
CREATE TYPE "Winner" AS ENUM ('P1', 'P2', 'NOP');

-- CreateTable
CREATE TABLE "Accounts" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "role" "AccountRole" NOT NULL DEFAULT 'USER',
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Accounts_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "GameUser" (
    "id" TEXT NOT NULL,
    "game_elo" INTEGER NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "account_id" TEXT NOT NULL,

    CONSTRAINT "GameUser_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "GameLog" (
    "id" TEXT NOT NULL,
    "game_type" "gameType" NOT NULL,
    "winner" "Winner" NOT NULL DEFAULT 'NOP',
    "duration" INTEGER NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "player_1" TEXT NOT NULL,
    "player_2" TEXT NOT NULL,
    "detail" TEXT NOT NULL,

    CONSTRAINT "GameLog_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "GameDetail" (
    "id" TEXT NOT NULL,
    "board" TEXT[],
    "p1_move" TEXT[],
    "p2_move" TEXT[],
    "move_count" INTEGER NOT NULL DEFAULT 0,

    CONSTRAINT "GameDetail_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "GameRoom" (
    "id" TEXT NOT NULL,
    "is_wait" BOOLEAN NOT NULL DEFAULT true,
    "creator" TEXT NOT NULL,
    "log" TEXT NOT NULL,

    CONSTRAINT "GameRoom_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Accounts_email_key" ON "Accounts"("email");

-- AddForeignKey
ALTER TABLE "GameUser" ADD CONSTRAINT "GameUser_account_id_fkey" FOREIGN KEY ("account_id") REFERENCES "Accounts"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "GameLog" ADD CONSTRAINT "GameLog_player_1_fkey" FOREIGN KEY ("player_1") REFERENCES "GameUser"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "GameLog" ADD CONSTRAINT "GameLog_player_2_fkey" FOREIGN KEY ("player_2") REFERENCES "GameUser"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "GameLog" ADD CONSTRAINT "GameLog_detail_fkey" FOREIGN KEY ("detail") REFERENCES "GameDetail"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "GameRoom" ADD CONSTRAINT "GameRoom_creator_fkey" FOREIGN KEY ("creator") REFERENCES "GameUser"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "GameRoom" ADD CONSTRAINT "GameRoom_log_fkey" FOREIGN KEY ("log") REFERENCES "GameLog"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
