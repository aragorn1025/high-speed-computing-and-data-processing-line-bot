CREATE TABLE `records` (
  `id` int(11) NOT NULL,
  `user_id` text NOT NULL,
  `record` text NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `records` (`id`, `user_id`, `record`, `timestamp`) VALUES
(1, 'Ufb68b93dd139ad3ed7a318305a15b281', 'hjgtuqirtetahbgnq', '2018-06-20 11:54:47'),
(2, 'Ufb68b93dd139ad3ed7a318305a15b281', 'hjgtuqirtetahbgnq', '2018-06-20 12:03:13'),
(3, 'Ufb68b93dd139ad3ed7a318305a15b281', '幫助', '2018-06-20 12:10:03'),
(4, 'Ufb68b93dd139ad3ed7a318305a15b281', '幫助', '2018-06-20 12:11:42'),
(5, 'Ufb68b93dd139ad3ed7a318305a15b281', '幫助', '2018-06-20 12:11:46'),
(6, 'Ufb68b93dd139ad3ed7a318305a15b281', '幫助 推薦', '2018-06-20 12:13:01'),
(7, 'Ufb68b93dd139ad3ed7a318305a15b281', '測試一二三', '2018-06-20 12:32:54'),
(8, 'Ufb68b93dd139ad3ed7a318305a15b281', '幫助 \'推薦', '2018-06-20 12:35:38'),
(9, 'Ufb68b93dd139ad3ed7a318305a15b281', '幫助 \'推薦', '2018-06-20 12:36:00'),
(10, 'Ufb68b93dd139ad3ed7a318305a15b281', '幫助 \'推薦', '2018-06-20 12:38:40'),
(11, 'Ufb68b93dd139ad3ed7a318305a15b281', '幫助 \'推薦\'\"\'\"\'', '2018-06-20 12:39:25'),
(12, 'Ued4cd6ea20e4d53a93e31a9fba5988b8', '你好', '2018-06-20 12:41:52'),
(13, 'Ued4cd6ea20e4d53a93e31a9fba5988b8', '推薦', '2018-06-20 12:41:58'),
(14, 'Ufb68b93dd139ad3ed7a318305a15b281', '幫助', '2018-06-20 13:11:01'),
(15, 'U2eee0fd28264422dca294fbcbc862c90', 'Hi', '2018-06-20 13:26:15'),
(16, 'U2eee0fd28264422dca294fbcbc862c90', '幫助 ', '2018-06-20 13:26:27'),
(17, 'U2eee0fd28264422dca294fbcbc862c90', '幫助 推薦', '2018-06-20 13:26:36'),
(18, 'U2eee0fd28264422dca294fbcbc862c90', '推薦', '2018-06-20 13:26:45'),
(19, 'U2eee0fd28264422dca294fbcbc862c90', '01', '2018-06-20 13:26:56'),
(20, 'U2eee0fd28264422dca294fbcbc862c90', '試聽', '2018-06-20 13:27:08'),
(21, 'U2eee0fd28264422dca294fbcbc862c90', '試聽 推薦 1', '2018-06-20 13:27:22'),
(22, 'U71e8b3fdd46ff45dd2629d1ac840183a', 'hi', '2018-06-20 13:50:28'),
(23, 'U71e8b3fdd46ff45dd2629d1ac840183a', '幫助', '2018-06-20 13:50:37'),
(24, 'U71e8b3fdd46ff45dd2629d1ac840183a', '推薦', '2018-06-20 13:50:43'),
(25, 'U71e8b3fdd46ff45dd2629d1ac840183a', '試聽', '2018-06-20 13:50:56'),
(26, 'U71e8b3fdd46ff45dd2629d1ac840183a', '試聽 推薦 7', '2018-06-20 13:51:12'),
(27, 'Ufb68b93dd139ad3ed7a318305a15b281', '幫助', '2018-06-21 02:10:55');

ALTER TABLE `records`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `records`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;
